"""
Multi-provider LLM client for generating paper summaries.
Supports: Kimi, OpenAI, Claude, Gemini, DeepSeek
"""

import json
import logging
import os
import time
from typing import Any, Optional

import requests


class LLMClient:
    """Unified LLM client supporting multiple providers."""

    def __init__(self, config: dict[str, Any]):
        self.config = config
        self.providers_config = config.get("providers", {})
        self.default_provider = config.get("default_provider", "deepseek")
        self.fallback_chain = config.get("fallback_chain", ["kimi", "openai", "rule_based"])
        self.model_name = self._get_model_name(self.default_provider)

    def _get_model_name(self, provider: str) -> str | None:
        """Get model name for provider."""
        provider_config = self.providers_config.get(provider, {})
        return provider_config.get("model")

    def _get_api_key(self, provider: str) -> Optional[str]:
        """Get API key for provider from environment."""
        provider_config = self.providers_config.get(provider, {})
        env_key = provider_config.get("env_key")
        if env_key:
            return os.getenv(env_key)
        return None
    
    def _call_kimi(self, messages: list[dict], temperature: float = 0.3) -> Optional[str]:
        """Call Kimi/Moonshot API."""
        api_key = self._get_api_key("kimi")
        if not api_key:
            return None
        
        config = self.providers_config["kimi"]
        
        try:
            response = requests.post(
                f"{config['api_base']}/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": config["model"],
                    "temperature": temperature,
                    "messages": messages
                },
                timeout=config.get("timeout", 90)
            )
            response.raise_for_status()
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except Exception as e:
            logging.warning(f"Kimi API error: {e}")
            return None
    
    def _call_openai(self, messages: list[dict], temperature: float = 0.3, model: str | None = None) -> Optional[str]:
        """Call OpenAI API. Pass `model` to override the configured default."""
        api_key = self._get_api_key("openai")
        if not api_key:
            return None

        config = self.providers_config["openai"]
        model_name = model or config["model"]

        payload = {"model": model_name, "messages": messages}
        # Some newer OpenAI models (e.g. gpt-5.5) only accept the default
        # temperature and reject an explicit value — omit it for those.
        if not model_name.startswith("gpt-5.5"):
            payload["temperature"] = temperature

        try:
            response = requests.post(
                f"{config['api_base']}/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json=payload,
                timeout=config.get("timeout", 90)
            )
            response.raise_for_status()
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except Exception as e:
            logging.warning(f"OpenAI API error: {e}")
            return None
    
    def _call_claude(self, messages: list[dict], temperature: float = 0.3) -> Optional[str]:
        """Call Anthropic Claude API."""
        api_key = self._get_api_key("claude")
        if not api_key:
            return None
        
        config = self.providers_config["claude"]
        
        # Convert messages to Claude format
        system_msg = ""
        user_msg = ""
        for msg in messages:
            if msg["role"] == "system":
                system_msg = msg["content"]
            elif msg["role"] == "user":
                user_msg = msg["content"]
        
        try:
            response = requests.post(
                f"{config['api_base']}/v1/messages",
                headers={
                    "x-api-key": api_key,
                    "Content-Type": "application/json",
                    "anthropic-version": "2023-06-01"
                },
                json={
                    "model": config["model"],
                    "max_tokens": 4096,
                    "temperature": temperature,
                    "system": system_msg,
                    "messages": [{"role": "user", "content": user_msg}]
                },
                timeout=config.get("timeout", 90)
            )
            response.raise_for_status()
            data = response.json()
            return data.get("content", [{}])[0].get("text", "")
        except Exception as e:
            logging.warning(f"Claude API error: {e}")
            return None
    
    def _call_gemini(self, messages: list[dict], temperature: float = 0.3) -> Optional[str]:
        """Call Google Gemini API."""
        api_key = self._get_api_key("gemini")
        if not api_key:
            return None
        
        config = self.providers_config["gemini"]
        
        # Convert messages to Gemini format
        contents = []
        for msg in messages:
            if msg["role"] == "user":
                contents.append({"role": "user", "parts": [{"text": msg["content"]}]})
            elif msg["role"] == "model" or msg["role"] == "assistant":
                contents.append({"role": "model", "parts": [{"text": msg["content"]}]})
        
        try:
            response = requests.post(
                f"{config['api_base']}/models/{config['model']}:generateContent",
                headers={"Content-Type": "application/json"},
                params={"key": api_key},
                json={
                    "contents": contents,
                    "generationConfig": {
                        "temperature": temperature,
                        "maxOutputTokens": 4096
                    }
                },
                timeout=config.get("timeout", 90)
            )
            response.raise_for_status()
            data = response.json()
            return data.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
        except Exception as e:
            logging.warning(f"Gemini API error: {e}")
            return None
    
    def _call_deepseek(self, messages: list[dict], temperature: float = 0.3) -> Optional[str]:
        """Call DeepSeek API with support for custom base URL."""
        api_key = self._get_api_key("deepseek")
        if not api_key:
            logging.warning("DeepSeek API key not found")
            return None

        config = self.providers_config["deepseek"]

        # Allow custom base URL via environment variable
        base_url = os.getenv("DEEPSEEK_API_BASE", config['api_base'])
        
        logging.debug(f"DeepSeek API: base_url={base_url}, model={config.get('model')}")

        try:
            response = requests.post(
                f"{base_url}/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": config["model"],
                    "temperature": temperature,
                    "messages": messages
                },
                timeout=config.get("timeout", 90)
            )
            logging.debug(f"DeepSeek API response: {response.status_code}")
            response.raise_for_status()
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except Exception as e:
            logging.warning(f"DeepSeek API error: {e}")
            return None

    def _call_dashscope(self, messages: list[dict], temperature: float = 0.3) -> Optional[str]:
        """Call DashScope (Aliyun) API."""
        api_key = self._get_api_key("dashscope")
        if not api_key:
            return None

        config = self.providers_config["dashscope"]

        try:
            response = requests.post(
                f"{config['api_base']}/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": config["model"],
                    "temperature": temperature,
                    "messages": messages
                },
                timeout=config.get("timeout", 90)
            )
            response.raise_for_status()
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except Exception as e:
            logging.warning(f"DashScope API error: {e}")
            return None

    def _call_provider(self, messages: list[dict], provider: str, temperature: float = 0.3) -> Optional[str]:
        """Call a specific provider."""
        if provider == "kimi":
            return self._call_kimi(messages, temperature)
        elif provider == "openai":
            return self._call_openai(messages, temperature)
        elif provider == "claude":
            return self._call_claude(messages, temperature)
        elif provider == "gemini":
            return self._call_gemini(messages, temperature)
        elif provider == "deepseek":
            return self._call_deepseek(messages, temperature)
        elif provider == "dashscope":
            return self._call_dashscope(messages, temperature)
        else:
            logging.warning(f"Unknown provider: {provider}")
            return None

    def _update_model_name(self, provider: str) -> None:
        """Update model name based on provider."""
        self.model_name = self._get_model_name(provider)
    
    def _parse_json_block(self, content: str) -> Any:
        """Strip markdown fences and parse a JSON payload from an LLM response."""
        content = content.strip()
        if content.startswith("```json"):
            content = content[7:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]
        return json.loads(content.strip())

    def _zh_style_rule(self, language: str) -> str:
        """Writing-style guidance appended to Chinese generation prompts."""
        if language != "zh":
            return ""
        return (
            "\n\n【中文写作硬性要求，必须严格遵守】\n"
            "1) 所有技术术语、方法名、模型名、数据集/benchmark 名一律保留英文原文，"
            "绝对不要翻译成中文。下列词（及类似的所有技术词）必须用英文写，违反即为错误：\n"
            "   agent / web agent / GUI agent（不要写“代理”“网页代理”“智能体”）、"
            "memory / memory module（不要写“记忆”“记忆模块”）、"
            "retrieval / dense retrieval（不要写“检索”“密集检索”）、"
            "GUI grounding、action planning（不要写“动作规划”）、"
            "prompt（不要写“提示”）、tool use（不要写“工具使用”）、"
            "in-context learning、reinforcement learning / RL、fine-tuning（不要写“微调”）、"
            "benchmark、baseline（不要写“基线”）、ablation（不要写“消融”）、"
            "trajectory、episodic、token、embedding 等。\n"
            "   句子主干用中文，把这些英文术语原样嵌进句子里，例如："
            "“给 web agent 加了一个 memory module，用 dense retrieval 把过去的 trajectory 调出来。”\n"
            "2) 写得通俗、具体、口语化，像当面跟同事讲清楚这篇 paper。避免空泛套话："
            "说“提升性能”必须讲清在哪个 benchmark、提升了什么指标多少。\n"
            "3) 不要堆砌辞藻或营销腔（如“显著”“强大”“潜力”这类空词少用）。"
        )

    def score_relevance(
        self,
        papers: list[dict],
        profile: str,
        batch_size: int = 20,
    ) -> list[dict[str, Any]] | None:
        """
        Score each paper 0-10 for relevance against a user interest profile.

        Args:
            papers: List of dicts with at least 'title' and 'abstract'.
            profile: Natural-language description of the user's research interests.
            batch_size: Number of papers scored per LLM call.

        Returns:
            List aligned with `papers`, each item {'score': int, 'reason': str},
            or None if every batch failed.
        """
        if not papers:
            return []

        results: list[dict[str, Any]] = []
        any_success = False

        for i in range(0, len(papers), batch_size):
            batch = papers[i:i + batch_size]
            batch_num = i // batch_size + 1

            system_prompt = (
                "You are a strict research-paper filter for a single researcher. "
                "Given that researcher's interest profile and a list of papers "
                "(each with an 'index', title, and abstract), rate how relevant each paper is "
                "to THEM on an integer scale from 0 (irrelevant) to 10 (must-read). Be "
                "discriminating: most papers on arXiv are NOT relevant to any one person, so "
                "the majority should score low. Only give 6+ to papers that clearly match the "
                "stated interests. Return ONLY a JSON array with exactly one object per input "
                "paper. Each object MUST include the same 'index' it was given, plus 'score' "
                "(integer 0-10) and 'reason' (a concise <=15-word phrase, in English, "
                "explaining the score). Do not reorder, merge, or omit any paper."
            )
            numbered = [
                {"index": j, "title": p.get("title", ""), "abstract": p.get("abstract", "")}
                for j, p in enumerate(batch)
            ]
            user_content = (
                "RESEARCHER INTEREST PROFILE:\n"
                f"{profile}\n\n"
                "PAPERS TO SCORE (JSON):\n"
                f"{json.dumps(numbered, ensure_ascii=False)}"
            )
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
            ]

            logging.info(f"Scoring relevance for batch {batch_num} ({len(batch)} papers)...")
            # Relevance scoring is a cheap, high-volume task — use the configured
            # score_model (a cheaper tier) when scoring through OpenAI.
            score_model = self.providers_config.get("openai", {}).get("score_model")
            if self.default_provider == "openai" and score_model:
                content = self._call_openai(messages, model=score_model)
            else:
                content = self._call_provider(messages, self.default_provider)
            if not content:
                for provider in self.fallback_chain:
                    if provider in ("rule_based", self.default_provider):
                        continue
                    content = self._call_provider(messages, provider)
                    if content:
                        break
                    time.sleep(1)

            batch_scores: list[dict[str, Any]] | None = None
            if content:
                try:
                    parsed = self._parse_json_block(content)
                    if isinstance(parsed, list):
                        batch_scores = parsed
                        any_success = True
                except json.JSONDecodeError as e:
                    logging.warning(f"Failed to parse relevance JSON for batch {batch_num}: {e}")

            # Align scores back to each paper by its 'index'. Falling back to
            # positional order only if the model omitted indices entirely keeps
            # the title and its reason from drifting apart.
            by_index: dict[int, dict[str, Any]] = {}
            if batch_scores:
                for pos, item in enumerate(batch_scores):
                    if not isinstance(item, dict):
                        continue
                    raw_idx = item.get("index", pos)
                    try:
                        idx = int(raw_idx)
                    except (TypeError, ValueError):
                        idx = pos
                    by_index[idx] = item

            for j in range(len(batch)):
                item = by_index.get(j, {})
                try:
                    score = int(round(float(item.get("score", 0))))
                except (TypeError, ValueError):
                    score = 0
                score = max(0, min(10, score))
                results.append({"score": score, "reason": str(item.get("reason", "")).strip()})

            if i + batch_size < len(papers):
                time.sleep(1)

        return results if any_success else None

    def deep_read_paper(self, paper: dict, language: str = "zh") -> dict[str, Any] | None:
        """
        Deeply read a single high-priority paper with the stronger model and
        return a fuller, length-adaptive analysis.

        Returns a dict with the same keys as generate_summaries items
        ('summary', 'achieved', 'limitations'), or None on failure.
        """
        lang_name = {"zh": "Chinese", "en": "English"}.get(language, language)
        provider_cfg = self.providers_config.get("openai", {})
        deep_model = provider_cfg.get("deep_read_model") or provider_cfg.get("model")

        system_prompt = (
            f"You are a senior AI-agents researcher writing a careful 'after-reading note' "
            f"in {lang_name} for a peer, about ONE paper. Read the title and abstract closely "
            f"and think hard before writing. Your goal is to cut to the essence: many papers "
            f"dress up a fundamentally simple idea in heavy language — say the core plainly in "
            f"one stroke (e.g. for a benchmark: what data was collected, what system/harness was "
            f"built, what experiments were run, and the key insight). If the work is genuinely "
            f"complex, explain it in proportionally more detail. Match length to substance: do "
            f"NOT pad simple ideas, do NOT over-compress complex ones.\n"
            f"Return ONLY a JSON object with:\n"
            f"- 'summary': a flowing paragraph in {lang_name} (roughly 3-6 sentences, longer only "
            f"if the work truly warrants it) that makes a smart colleague grasp the essence fast: "
            f"the real motivation, the core mechanism/idea stated plainly, and why it matters. "
            f"Lead with the one-sentence essence, then unfold.\n"
            f"- 'achieved': 1-3 sentences in {lang_name} on what it concretely accomplished — "
            f"contributions and concrete reported results/numbers from the abstract.\n"
            f"- 'limitations': 1-3 sentences in {lang_name} — your critical read of what a strong "
            f"paper on this exact problem would have done but this one did not: missing baselines, "
            f"experiments, settings, ablations, or unsupported claims. Be specific and honest.\n"
            f"Ground claims in the abstract; do not invent numbers, but you may reason about gaps."
            + self._zh_style_rule(language)
        )
        user_content = json.dumps(
            {"title": paper.get("title", ""), "abstract": paper.get("abstract", "")},
            ensure_ascii=False,
        )
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        content = self._call_openai(messages, temperature=0.4, model=deep_model)
        if not content:
            return None
        try:
            parsed = self._parse_json_block(content)
        except json.JSONDecodeError as e:
            logging.warning(f"Deep-read JSON parse failed: {e}")
            return None
        if not isinstance(parsed, dict):
            return None
        return {
            "summary": str(parsed.get("summary", "")).strip(),
            "achieved": str(parsed.get("achieved", "")).strip(),
            "limitations": str(parsed.get("limitations", "")).strip(),
        }

    def generate_summaries(
        self,
        papers: list[dict],
        language: str = "zh",
        batch_size: int = 3
    ) -> tuple[list[dict[str, Any]] | None, str | None]:
        """
        Generate summaries for papers using available LLM providers.

        Args:
            papers: List of paper dicts with title, abstract, category
            language: Target language code (zh, en, ja, ko, etc.)
            batch_size: Number of papers per batch

        Returns:
            Tuple of (list of summaries or None, provider name used or None)
        """
        if not papers:
            return None, None
        
        language_names = {
            "zh": "Chinese",
            "en": "English",
            "ja": "Japanese",
            "ko": "Korean",
            "de": "German",
            "fr": "French",
            "es": "Spanish"
        }
        lang_name = language_names.get(language, language)
        
        all_results = []
        used_provider = None

        for i in range(0, len(papers), batch_size):
            batch = papers[i:i + batch_size]
            
            # Build prompt
            system_prompt = (
                f"You are a sharp, senior researcher in AI agents writing a digest for a "
                f"peer. For each paper, read the abstract carefully and write your own "
                f"critical take in {lang_name} — do NOT just paraphrase the abstract. "
                f"Return a JSON array with one object per paper IN THE SAME ORDER, each with:\n"
                f"- 'summary': 2-3 plain-language sentences in {lang_name} that let the reader "
                f"grasp the core idea fast — what problem it tackles, the key idea, and why it "
                f"matters. Avoid jargon and marketing language; explain it like to a smart colleague.\n"
                f"- 'achieved': 1-2 sentences in {lang_name} stating concretely what this paper "
                f"actually accomplished — its real contribution and any reported results/metrics.\n"
                f"- 'limitations': 1-2 sentences in {lang_name} with your critical read of what it "
                f"did NOT do. Think like an expert who was asked to tackle this same title: what "
                f"obvious experiments, baselines, settings, or claims a strong paper on this topic "
                f"would include but this one is missing or leaves unaddressed. Be specific and "
                f"honest, not generic. If the abstract truly gives no basis to judge, say so briefly.\n"
                f"Ground everything in the abstract; do not fabricate specific numbers not present, "
                f"but you MAY reason about gaps the abstract implies."
                + self._zh_style_rule(language)
            )

            user_content = json.dumps(batch, ensure_ascii=False)
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ]
            
            # Try default provider first, then fall back to fallback_chain
            content = None

            # First try the default provider
            logging.info(f"Trying default provider {self.default_provider} for batch {i//batch_size + 1}...")
            content = self._call_provider(messages, self.default_provider)
            if content:
                logging.info(f"Successfully used {self.default_provider}")
                used_provider = self.default_provider
                self._update_model_name(self.default_provider)
            else:
                # Default provider failed, try fallback chain
                for provider in self.fallback_chain:
                    if provider == "rule_based":
                        continue
                    if provider == self.default_provider:
                        continue  # Skip already tried default provider

                    logging.info(f"Trying {provider} for batch {i//batch_size + 1}...")
                    content = self._call_provider(messages, provider)
                    if content:
                        logging.info(f"Successfully used {provider}")
                        used_provider = provider
                        self._update_model_name(provider)
                        break

                    time.sleep(1)  # Brief delay between providers

            if not content:
                logging.warning(f"All LLM providers failed for batch {i//batch_size + 1}")
            else:
                # Parse JSON from content
                try:
                    # Remove markdown code blocks if present
                    content = content.strip()
                    if content.startswith("```json"):
                        content = content[7:]
                    if content.startswith("```"):
                        content = content[3:]
                    if content.endswith("```"):
                        content = content[:-3]
                    content = content.strip()

                    parsed = json.loads(content)
                    if isinstance(parsed, list):
                        all_results.extend(parsed)
                    else:
                        logging.warning(f"Unexpected response format from LLM")
                except json.JSONDecodeError as e:
                    logging.warning(f"Failed to parse LLM response as JSON: {e}")

            # Delay between batches
            if i + batch_size < len(papers):
                time.sleep(2)
        
        return (all_results if all_results else None), self.model_name


def create_client(config: dict) -> LLMClient:
    """Factory function to create LLM client from config."""
    return LLMClient(config)
