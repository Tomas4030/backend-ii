# Session 14 - Design de Entrega CrewAI

Data: 2026-05-08
Topico: Introducao a AI Agents em Python com CrewAI
Projeto alvo: `tomas/`

## 1) Contexto

Foi analisado o estado atual do repositorio `session14`, com foco no projeto `tomas/`.
O projeto ja esta perto do Quickstart oficial de Flows da CrewAI e usa:

- `Flow` com estado (`ResearchFlowState`)
- `Crew` com 2 agentes (`researcher`, `reporting_analyst`)
- `SerperDevTool` para pesquisa web
- output em `output/report.md`

Tambem foi validado o estado da stack antes de qualquer mudanca:

- Versao instalada de CrewAI: `1.14.4`
- Ultima versao no PyPI: `1.14.4`
- Changelog e Quickstart oficiais revistos

## 2) Objetivo da entrega

Fechar a Session 14 com uma entrega pronta para aula, em Portugues, com:

1. execucao funcional (`crewai run` sem erro)
2. geracao de relatorio (`output/report.md`)
3. explicacao teorica clara sobre AI Agents
4. guia curto de apresentacao para demonstracao em aula

## 3) Nao objetivos

- Nao recriar projeto novo de raiz
- Nao fazer refatoracao profunda sem impacto na entrega
- Nao introduzir funcionalidades fora do escopo introdutorio

## 4) Abordagem escolhida

Abordagem incremental sobre `tomas/` (recomendada e aprovada).

Racional:

- reduz risco e tempo
- aproveita estrutura ja funcional
- facilita demonstracao com foco no essencial da Session 14

## 5) Design tecnico

### 5.1 Arquitetura

Manter a arquitetura Flow + Crew:

- `prepare_topic` define topico e ano
- `run_research` executa `TomasCrew().crew().kickoff(inputs=...)`
- `save_report` confirma local do relatorio

### 5.2 Componentes e ajustes planeados

- `src/tomas/main.py`
  - garantir entrypoint coerente para execucao da Flow
  - manter estado simples e logs legiveis para demo

- `src/tomas/crew.py`
  - manter processo sequencial e `SerperDevTool`
  - validar consistencia entre nomes de metodos e YAML

- `src/tomas/config/agents.yaml`
  - ajustar texto para papeis claros e didaticos

- `src/tomas/config/tasks.yaml`
  - reforcar formato esperado do output em markdown
  - garantir escrita final em `output/report.md`

- `pyproject.toml`
  - alinhar scripts com funcoes realmente existentes
  - preservar `type = "flow"`

- Documentacao em PT
  - atualizar `README.md` com setup, run e troubleshooting
  - criar `APRESENTACAO.md` com roteiro de demo
  - incluir explicacao teorica de AI Agents para contexto de aula

## 6) Fluxo de dados

Input:

- topico default: `AI LLMs` (ou via trigger payload)

Pipeline:

1. Flow recebe topico e atualiza estado
2. Crew executa tarefas sequenciais
3. resultado final e persistido em `output/report.md`
4. resumo final fica no estado da Flow (`state.report`)

## 7) Tratamento de erros

- Falta de `SERPER_API_KEY`: documentar requisito e mensagem de diagnostico
- Erro de ambiente/dependencias: passos de verificacao rapida no README
- Erro de entrypoint/import: corrigir scripts e caminhos de modulo

## 8) Validacao e criterios de aceite

Entrega considerada pronta quando:

1. `crewai run` termina sem crash
2. `output/report.md` existe e tem conteudo estruturado
3. README permite reproducao local sem ambiguidades
4. guia de apresentacao permite demo em 3-5 minutos
5. explicacao teorica cobre definicao, tipos e casos de uso de AI Agents

## 9) Testes de verificacao

- smoke test de execucao da Flow
- verificacao de artefacto gerado (`output/report.md`)
- revisao manual da documentacao final em PT

## 10) Riscos e mitigacoes

- Dependencia de chave externa (Serper)
  - mitigacao: checklist de ambiente antes da demo

- Mudancas no entrypoint quebrarem comandos
  - mitigacao: alinhar scripts e validar comando final `crewai run`

- Documentacao extensa mas pouco pratica
  - mitigacao: criar secao de "comandos minimos" e roteiro de apresentacao

## 11) Entregaveis finais

- Codigo ajustado em `tomas/` com Flow funcional
- `output/report.md` gerado em execucao real
- README em PT atualizado
- `APRESENTACAO.md` com guiao de demonstracao
- explicacao teorica de AI Agents integrada na documentacao
