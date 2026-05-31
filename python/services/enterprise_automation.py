from datetime import UTC, datetime
from typing import TypedDict

PROCESS_MAP = [
    {
        "step": "Coleta de demandas",
        "process_input": "tickets internos e solicitações por formulário",
        "rules": "validar campos obrigatórios e prioridade",
        "output": "fila operacional priorizada",
    },
    {
        "step": "Processamento operacional",
        "process_input": "fila priorizada",
        "rules": "aplicar regras de SLA e responsável por área",
        "output": "tarefas distribuídas com prazo",
    },
    {
        "step": "Relatório executivo",
        "process_input": "tarefas concluídas e pendentes",
        "rules": "consolidar KPI diário e exceções",
        "output": "painel de operação para gestão",
    },
]


class ProcessStep(TypedDict):
    step: str
    process_input: str
    rules: str
    output: str


class PipelineStep(TypedDict):
    name: str
    description: str


class EnvironmentProfile(TypedDict):
    name: str
    purpose: str
    has_strict_controls: bool
    is_active: bool


class OperationalSummary(TypedDict):
    pipeline_health: str
    sla_compliance: str
    critical_alerts: int


class OperationalReport(TypedDict):
    summary: OperationalSummary
    priority_actions: list[str]


class EnterpriseAutomationPayload(TypedDict):
    objective: str
    process_map: list[ProcessStep]
    unified_pipeline: list[PipelineStep]
    environments: list[EnvironmentProfile]
    operational_report: OperationalReport
    monitoring: list[str]
    generated_at: str


class OperationalReportPayload(OperationalReport):
    generated_at: str


def _automation_goal() -> str:
    return (
        "Automatizar o fluxo operacional da empresa com um pipeline único, "
        "rastreável e orientado por indicadores."
    )


def _build_pipeline() -> list[PipelineStep]:
    return [
        {"name": "coleta", "description": "Captura e valida as entradas de negócio."},
        {
            "name": "processamento",
            "description": "Aplica regras, distribui tarefas e acompanha SLA.",
        },
        {"name": "relatorio", "description": "Publica visão operacional para decisão."},
    ]


def _environment_profiles(active_environment: str) -> list[EnvironmentProfile]:
    profiles = [
        {
            "name": "development",
            "purpose": "experimentação e ajustes locais",
            "has_strict_controls": False,
        },
        {
            "name": "homologation",
            "purpose": "validação com dados de negócio mascarados",
            "has_strict_controls": True,
        },
        {
            "name": "production",
            "purpose": "operação oficial da empresa",
            "has_strict_controls": True,
        },
    ]

    for profile in profiles:
        profile["is_active"] = profile["name"] == active_environment
    return profiles


def _operational_report() -> OperationalReport:
    return {
        "summary": {
            "pipeline_health": "estável",
            "sla_compliance": "95%",
            "critical_alerts": 0,
        },
        "priority_actions": [
            "Revisar backlog diário às 09:00",
            "Validar pendências de SLA no fechamento do dia",
            "Registrar incidentes operacionais em log de auditoria",
        ],
    }


def _monitoring_plan() -> list[str]:
    return [
        "Acompanhar endpoint /health continuamente",
        "Revisar relatório operacional diário",
        "Executar ciclo de melhoria contínua semanal",
    ]


def get_enterprise_automation_payload(
    active_environment: str,
) -> EnterpriseAutomationPayload:
    return {
        "objective": _automation_goal(),
        "process_map": PROCESS_MAP,
        "unified_pipeline": _build_pipeline(),
        "environments": _environment_profiles(active_environment),
        "operational_report": _operational_report(),
        "monitoring": _monitoring_plan(),
        "generated_at": datetime.now(UTC).isoformat(),
    }


def get_operational_report_payload() -> OperationalReportPayload:
    report = _operational_report()
    return {
        "summary": report["summary"],
        "priority_actions": report["priority_actions"],
        "generated_at": datetime.now(UTC).isoformat(),
    }
