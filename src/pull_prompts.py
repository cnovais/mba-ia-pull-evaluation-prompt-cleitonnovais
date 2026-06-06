"""
Script para fazer pull de prompts do LangSmith Prompt Hub.

Este script:
1. Conecta ao LangSmith usando credenciais do .env
2. Faz pull dos prompts do Hub
3. Salva localmente em prompts/bug_to_user_story_v1.yml

SIMPLIFICADO: Usa serialização nativa do LangChain para extrair prompts.
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from langchain import hub
from utils import save_yaml, check_env_vars, print_section_header

#minhas alterações
from langsmith import Client

load_dotenv()

client = Client()

def save_prompt_locally(prompt):
    Path("prompts").mkdir(exist_ok=True)
    system_template = prompt.messages[0].prompt.template
    human_template = prompt.messages[1].prompt.template

    with open("prompts/bug_to_user_story_v1.yml", "w", encoding="utf-8") as f:
        f.write(system_template + "\n\n" + human_template)

    print("Prompt salvo localmente")

def pull_prompts_from_langsmith():
    prompt = client.pull_prompt("leonanluppi/bug_to_user_story_v1")
    print(f"Prompt '{prompt.name}' puxado do LangSmith Hub")
    return prompt


def main():
    """Função principal"""
    prompt = pull_prompts_from_langsmith()
    save_prompt_locally(prompt)


if __name__ == "__main__":
    sys.exit(main())
