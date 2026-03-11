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
        self.provider = config.get("default_provider", "kimi")
        self.providers_config = config.get("providers", {})
        self.fallback_chain = config.get("fallback_chain", ["kimi", "openai", "rule_based"])
    
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
    
    def _call_openai(self, messages: list[dict], temperature: float = 0.3) -> Optional[str]:
        """Call OpenAI API."""
        api_key = self._get_api_key("openai")
        if not api_key:
            return None
        
        config = self.providers_config["openai"]
        
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
            return None
        
        config = self.providers_config["deepseek"]
        
        # Allow custom base URL via environment variable
        base_url = os.getenv("DEEPSEEK_API_BASE", config['api_base'])
        
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
            response.raise_for_status()
            data = response.json()
            return data.get("choices", [{}])[0].get("message", {}).get("content", "")
        except Exception as e:
            logging.warning(f"DeepSeek API error: {e}")
            return None
    
    def generate_summaries(
        self,
        papers: list[dict],
        language: str = "zh",
        batch_size: int = 3
    ) -> list[dict[str, Any]] | None:
        """
        Generate summaries for papers using available LLM providers.
        
        Args:
            papers: List of paper dicts with title, abstract, category
            language: Target language code (zh, en, ja, ko, etc.)
            batch_size: Number of papers per batch
        
        Returns:
            List of summaries or None if all providers fail
        """
        if not papers:
            return None
        
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
        
        for i in range(0, len(papers), batch_size):
            batch = papers[i:i + batch_size]
            
            # Build prompt
            system_prompt = (
                f"You are a research assistant. For each paper, provide a summary in {lang_name}. "
                f"Return a JSON array where each item has keys 'summary' (2-4 sentence summary in {lang_name}) "
                f"and 'readability' (one sentence readability analysis in {lang_name}). "
                f"Be faithful to the abstract. Do not invent claims not present in the text."
            )
            
            user_content = json.dumps(batch, ensure_ascii=False)
            messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content}
            ]
            
            # Try providers in fallback chain
            content = None
            for provider in self.fallback_chain:
                if provider == "rule_based":
                    continue
                
                logging.info(f"Trying {provider} for batch {i//batch_size + 1}...")
                
                if provider == "kimi":
                    content = self._call_kimi(messages)
                elif provider == "openai":
                    content = self._call_openai(messages)
                elif provider == "claude":
                    content = self._call_claude(messages)
                elif provider == "gemini":
                    content = self._call_gemini(messages)
                elif provider == "deepseek":
                    content = self._call_deepseek(messages)
                
                if content:
                    logging.info(f"Successfully used {provider}")
                    break
                
                time.sleep(1)  # Brief delay between providers
            
            if content:
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
            else:
                logging.warning(f"All LLM providers failed for batch {i//batch_size + 1}")
            
            # Delay between batches
            if i + batch_size < len(papers):
                time.sleep(2)
        
        return all_results if all_results else None


def create_client(config: dict) -> LLMClient:
    """Factory function to create LLM client from config."""
    return LLMClient(config)
