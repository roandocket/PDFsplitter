# Guia de Contribuição

## Como Contribuir

### 1. Configuração Inicial
```bash
git clone <repositorio>
cd PdfManipulator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Fluxo de Trabalho
1. **Criar branch**: `git checkout -b feature/nome-da-feature`
2. **Desenvolver**: Implementar funcionalidade
3. **Testar**: Executar testes e validar
4. **Commit**: `git commit -m "feat: descrição da mudança"`
5. **Push**: `git push origin feature/nome-da-feature`
6. **Pull Request**: Criar PR para revisão

### 3. Padrões de Commit
```
feat: nova funcionalidade
fix: correção de bug
docs: documentação
test: testes
refactor: refatoração
style: formatação
```

### 4. Code Review
- Revisar código do colega
- Fornecer feedback construtivo
- Aprovar apenas após validação

### 5. Documentação
- Registrar decisões em `docs/DECISIONS.md`
- Atualizar documentação quando necessário
- Comentar código complexo

## Boas Práticas

### Código
- Nomes descritivos para variáveis/funções
- Funções pequenas e focadas
- Tratamento de erros adequado
- Documentação clara

### Testes
- Testar casos de sucesso e erro
- Usar nomes descritivos para testes
- Manter testes atualizados

### Comunicação
- Ser claro e objetivo
- Perguntar quando em dúvida
- Compartilhar conhecimento

## Estrutura de Desenvolvimento

### 1. Planejamento
- Definir tarefa claramente
- Documentar decisões técnicas
- Estimar tempo necessário

### 2. Implementação
- Seguir padrões estabelecidos
- Implementar testes junto
- Manter logs informativos

### 3. Validação
- Executar todos os testes
- Verificar qualidade do código
- Validar funcionalidade

### 4. Documentação
- Atualizar documentação
- Registrar mudanças importantes
- Comentar decisões complexas

## Ferramentas Recomendadas

### IDE/Editor
- **VS Code**: Extensões Python, Git
- **PyCharm**: Debugger integrado
- **Vim/Emacs**: Para usuários avançados

### Debug
- **pdb**: Debugger Python
- **logging**: Logs estruturados
- **print**: Para debug rápido

### Qualidade
- **pylint**: Análise estática
- **black**: Formatação automática
- **isort**: Organização de imports

## Processo de Revisão

### 1. Preparação
- Código limpo e documentado
- Testes passando
- Commits organizados

### 2. Submissão
- Descrição clara da mudança
- Contexto da implementação
- Impacto esperado

### 3. Revisão
- Verificar lógica
- Validar testes
- Checar documentação

### 4. Aprovação
- Todos os pontos atendidos
- Feedback incorporado
- Pronto para merge

## Resolução de Conflitos

### 1. Identificação
- Git mostrará conflitos
- Analisar mudanças conflitantes
- Entender contexto

### 2. Resolução
- Decidir qual mudança manter
- Combinar quando possível
- Testar após resolução

### 3. Validação
- Executar testes
- Verificar funcionalidade
- Confirmar com equipe

## Comunicação

### Canais
- **Issues**: Para bugs e melhorias
- **Pull Requests**: Para discussões de código
- **DECISIONS.md**: Para decisões técnicas

### Reuniões
- **Daily**: 15 min para alinhamento
- **Review**: Semanal para revisão de progresso
- **Retrospectiva**: Quinzenal para melhorias

## Recursos Úteis

### Documentação
- [Python Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Git Flow](https://nvie.com/posts/a-successful-git-branching-model/)
- [Conventional Commits](https://www.conventionalcommits.org/)

### Ferramentas
- [Regex101](https://regex101.com/): Testar regex
- [PDF Tools](https://pypdf.readthedocs.io/): Documentação pypdf
- [ReportLab](https://www.reportlab.com/docs/reportlab-userguide.pdf): Guia ReportLab

## Suporte

### Dúvidas Técnicas
- Consultar documentação
- Pesquisar em issues
- Perguntar para equipe

### Problemas
- Criar issue detalhada
- Incluir logs e contexto
- Propor solução se possível

---

**Lembre-se**: Trabalho em equipe é colaboração, não competição! 🤝 