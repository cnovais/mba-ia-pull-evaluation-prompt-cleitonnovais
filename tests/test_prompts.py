"""
Testes automatizados para validação de prompts.
"""
import pytest
import yaml
import sys
from pathlib import Path

# Adicionar src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from utils import validate_prompt_structure

def load_prompts(file_path: str):
    """Carrega prompts do arquivo YAML."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

class TestPrompts:
    def test_prompt_has_system_prompt(self):
        prompt = load_prompts("prompts/bug_to_user_story_v2.yml")
        prompt_data_system_prompt = prompt["bug_to_user_story_v2"]["system_prompt"]
        
        assert prompt_data_system_prompt is not None, "system_prompt não deve ser None"
        assert isinstance(prompt_data_system_prompt, str), "system_prompt deve ser uma string"
        assert len(prompt_data_system_prompt.strip()) > 0, "system_prompt não deve estar vazio"

    def test_prompt_has_role_definition(self):
        """Verifica se o prompt define uma persona (ex: "Você é um Product Manager")."""
        prompt = load_prompts("prompts/bug_to_user_story_v2.yml")
        prompt_data_system_prompt = prompt["bug_to_user_story_v2"]["system_prompt"]
        
        assert prompt_data_system_prompt is not None, "system_prompt não deve ser None"
        assert isinstance(prompt_data_system_prompt, str), "system_prompt deve ser uma string"
        assert len(prompt_data_system_prompt.strip()) > 0, "system_prompt não deve estar vazio"
        
        assert "Você é um Product Owner" in prompt_data_system_prompt, "system_prompt deve definir uma persona com 'Você é'"

    def test_prompt_mentions_format(self):
        """Verifica se o prompt exige formato Markdown ou User Story padrão."""
        prompt = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = prompt["bug_to_user_story_v2"]["system_prompt"]

        format_keywords = ["Como um", "Critérios de Aceitação", "Dado que"]

        assert any(keyword in system_prompt for keyword in format_keywords), \
            f"system_prompt deve mencionar pelo menos um dos formatos: {format_keywords}"

    def test_prompt_has_few_shot_examples(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        prompt = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = prompt["bug_to_user_story_v2"]["system_prompt"]

        format_keywords = ["EXEMPLOS DE REFERÊNCIA"]

        assert any(keyword in system_prompt for keyword in format_keywords), \
            f"system_prompt tem que ter EXEMPLOS DE REFERÊNCIA: {format_keywords}"

    def test_prompt_no_todos(self):
        """Garante que você não esqueceu nenhum `[TODO]` no texto."""
        prompt = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = prompt["bug_to_user_story_v2"]["system_prompt"]

        assert "[TODO]" not in system_prompt, "system_prompt contém [TODO] não resolvido"

    def test_minimum_techniques(self):
        """Verifica se o prompt contém exemplos de entrada/saída (técnica Few-shot)."""
        prompt = load_prompts("prompts/bug_to_user_story_v2.yml")
        system_prompt = prompt["bug_to_user_story_v2"]["system_prompt"]

        few_shot_keywords = ["Input:", "Output:"]

        assert all(keyword in system_prompt for keyword in few_shot_keywords), \
            f"system_prompt deve conter exemplos few-shot com: {few_shot_keywords}"

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])