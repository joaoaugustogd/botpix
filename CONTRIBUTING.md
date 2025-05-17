# Guia de Contribuição

Obrigado por seu interesse em contribuir para o projeto **Botpix**\! Valorizo muito a ajuda da comunidade para tornar este projeto ainda melhor.

Este guia tem como objetivo fornecer um roteiro claro para que você possa contribuir de forma eficaz e colaborativa.

## Como Você Pode Contribuir

Existem várias maneiras pelas quais você pode contribuir para este projeto:

* **Reportar Bugs:** Se você encontrar algum problema ou comportamento inesperado, por favor, abra uma nova Issue no GitHub. Seja o mais detalhado possível na sua descrição, incluindo os passos para reproduzir o bug, o comportamento esperado e o comportamento real.
* **Sugerir Melhorias e Novas Funcionalidades:** Se você tem ideias para melhorar o chatbot, adicionar novas funcionalidades ou otimizar o código, sinta-se à vontade para abrir uma nova Issue com sua sugestão. Explique claramente sua ideia e os benefícios que ela traria ao projeto.
* **Contribuir com Código:** Se você deseja contribuir com código diretamente, seja para corrigir bugs ou implementar novas funcionalidades, siga o fluxo de Pull Request descrito abaixo.
* **Melhorar a Documentação:** A documentação é crucial para qualquer projeto. Se você encontrar áreas que precisam de mais clareza, correções ou informações adicionais, você pode contribuir abrindo uma Issue ou enviando um Pull Request com suas melhorias.
* **Testar:** Ajudar a testar novas funcionalidades e correções de bugs é fundamental para garantir a qualidade do projeto. Se você tiver interesse em testar, fique de olho nas Issues e Pull Requests abertos.

## Fluxo de Contribuição com Código (Pull Requests)

1.  **Faça um Fork do Repositório:** Na página do projeto no GitHub, clique no botão "Fork" no canto superior direito. Isso criará uma cópia do repositório na sua conta.

2.  **Clone o Seu Fork:** Clone o repositório para o seu ambiente local:
    ```bash
    git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
    cd NOME_DO_REPOSITORIO
    ```
    (Substitua `SEU_USUARIO` pelo seu nome de usuário do GitHub e `NOME_DO_REPOSITORIO` pelo nome do repositório forkado).

3.  **Crie um Branch:** Crie um branch para a sua contribuição. Dê um nome descritivo ao seu branch (ex: `feature/nova-funcionalidade`, `fix/bug-de-pagamento`):
    ```bash
    git checkout -b nome-do-seu-branch
    ```

4.  **Faça suas Alterações:** Implemente suas correções ou novas funcionalidades no código. Siga as convenções de código existentes e tente manter suas alterações focadas em um único objetivo.

5.  **Adicione e Commite suas Alterações:**
    ```bash
    git add .
    git commit -m "Breve descrição da sua alteração"
    ```
    Escreva mensagens de commit claras e concisas, explicando o que você modificou e por quê.

6.  **Faça Push para o Seu Fork:**
    ```bash
    git push origin nome-do-seu-branch
    ```

7.  **Abra um Pull Request (PR):** Na página do seu fork no GitHub, você verá um botão "Compare & pull request". Clique nele.

8.  **Descreva o Seu Pull Request:** Forneça um título claro e uma descrição detalhada do seu Pull Request. Explique o que você fez, por que fez e quaisquer detalhes relevantes para os revisores. Se o seu PR resolve alguma Issue específica, mencione `#ID_DA_ISSUE` na descrição.

9.  **Aguarde a Revisão:** Os mantenedores do projeto revisarão o seu Pull Request. Eles podem solicitar alterações ou fazer perguntas. Esteja aberto a feedback e disposto a fazer as modificações necessárias.

10. **Merge:** Uma vez que o seu Pull Request seja aprovado, ele será mergeado para o branch principal do projeto. Parabéns, sua contribuição foi integrada\!

## Diretrizes de Código

* Siga as convenções de estilo de código existentes no projeto.
* Escreva código claro, legível e bem comentado.
* Inclua testes unitários para suas alterações, se aplicável.
* Certifique-se de que seu código não introduza novos bugs.

## Relatando Bugs

Ao reportar um bug, inclua as seguintes informações, se possível:

* O sistema operacional e a versão do Python que você está usando.
* Os passos exatos para reproduzir o bug.
* O comportamento esperado.
* O comportamento real que você observou.
* Qualquer mensagem de erro ou traceback relevante.

## Sugestões de Melhorias

Ao sugerir melhorias, tente ser o mais específico possível sobre a mudança que você gostaria de ver e os benefícios que ela traria. Se possível, inclua exemplos de como a funcionalidade poderia ser implementada ou usada.

## Seja Respeitoso

Mantenha um tom respeitoso e construtivo em todas as suas interações com outros colaboradores e mantenedores do projeto.

Agradecemos novamente a sua contribuição\!
