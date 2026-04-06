import json
import sys

def synthesize_report(raw_data):
    """
    Synthesizes expert growth insights based on raw Instagram metrics.
    """
    niche = raw_data.get("niche", "Geral")
    reach = raw_data.get("reach", 0)
    
    # Heuristic logic for the 7-day plan
    plan = []
    if niche == "Imobiliário":
        plan = [
            {"task": "Criar 3 Reels de 'Tour Rápido' sem trilha sonora alta.", "priority": "Alta"},
            {"task": "Destaque 'Depoimentos' deve ter no mínimo 5 provas sociais.", "priority": "Crítica"}
        ]
    elif niche == "Saúde":
        plan = [
            {"task": "Postar 1 vídeo explicativo sobre um mito comum do setor.", "priority": "Alta"},
            {"task": "Humanizar a Bio: Substituir termos técnicos por benefícios.", "priority": "Média"}
        ]
    else:
        plan = [
            {"task": "Focar em 3 postagens de engajamento direto (Enquetes).", "priority": "Média"}
        ]

    report = {
        "score": round(min(10, reach / 5000 + 5), 1),
        "plan": plan,
        "summary": f"O perfil de {niche} apresenta um potencial latente. O foco deve ser em retenção de vídeo."
    }
    return report

if __name__ == "__main__":
    mock_raw = {"niche": "Imobiliário", "reach": 12500}
    final_report = synthesize_report(mock_raw)
    print(json.dumps(final_report, indent=4, ensure_ascii=False))
