/*------------ SHOW MENU-------------*/
const showMneu = (toggleId, navId) => {
    const toggle = document.getElementById(toggleId),
        nav = document.getElementById(navId)
    /*valida se se existe as variaveis*/
    if (toggle && nav) {
        /*aqui adiciono a class show-menu na div com a class nav__menu*/
        toggle.addEventListener('click', () => {
            /*adicina a class show-menu na div que tem o id nav-menu */
            nav.classList.toggle('show-menu')
        })
    }
}
showMneu('nav-toggle', 'nav')

/*------------ REMOVER MENU MOBILE -------------*/
const navLink = document.querySelectorAll('.nav__link')
function linkAction() {
    const navMenu = document.getElementById('nav')
    /*Quando um link ou o botão close for clicado a class show-menu será removido*/
    navMenu.classList.remove('show-menu')
}
navLink.forEach(n => n.addEventListener('click', linkAction))

/*==================== DEIXA O LINK CLICADO COM A CLASS ACTIVE-LINK ====================*/
const linkColor = document.querySelectorAll('.nav__link')

function colorLink(){
    if(linkColor){
        linkColor.forEach(L => L.classList.remove('active-link'))
        this.classList.add('active-link')
    }
}

linkColor.forEach(L=> L.addEventListener('click', colorLink))
/*==================== MUDAR A COR DO HEADER ====================*/
function scrollHeader(){
    const scrollHeader = document.getElementById('header')
    if(this.scrollY >= 100) scrollHeader.classList.add('scroll-header'); else scrollHeader.classList.remove('scroll-header')

}
window.addEventListener('scroll', scrollHeader)


fetch('http://127.0.0.1:8000/images/')
    .then(response => response.json())
    .then(data => {
        // Preenche a tabela com os dados da API
        
        const listaDeImagens = document.getElementById('listaImagens')

        data.forEach(element => {
            const imagem = document.createElement('img')
            imagem.src = element.imagem
            const div = document.createElement('div')
            div.classList.add('gallery__img')
            div.appendChild(imagem)
            listaDeImagens.appendChild(div)

        });
        
    })
    .catch(error => console.error(error));

fetch('http://127.0.0.1:8000/servicos/')
    .then(response => response.json())
    .then(data => {
        // Preenche a tabela com os dados da API
        
        const listaDeImagens = document.getElementById('lista_servicos')

        data.forEach(element => {
            const div = document.createElement('div')
            div.classList.add('box')
            const div2 = document.createElement('div')
            div2.classList.add('inner')

            const img = document.createElement('img')
            img.src = element.picture
            
            const p = document.createElement('p')
            p.textContent = element.nome

            div2.appendChild(img)
            div2.appendChild(p)
            div.appendChild(div2)
            listaDeImagens.appendChild(div)

        });
        
    })
    .catch(error => console.error(error));
	
fetch('http://127.0.0.1:8000/comentarios/')
    .then(response => response.json())
    .then(data => {
        
        const listaDeComentarios = document.getElementById('lista_comentarios')

        data.forEach(element => {
            const div = document.createElement('div')
            div.classList.add('viewer')

            const h4 = document.createElement('h4')
            h4.textContent = element.nome_usuario
            const p = document.createElement('p')
            p.textContent = element.comentario
            
            div.appendChild(h4)
            div.appendChild(p)
            listaDeComentarios.appendChild(div)

        });
        
    })
    .catch(error => console.error(error));
	


const formulario = document.querySelector('#comentario');

formulario.addEventListener('submit', async (event) => {
    // Impede que a página seja redirecionada para a API
    event.preventDefault();

    // Obtém os dados do formulário
    const dadosDoFormulario = new FormData(formulario);

    try {
    // Envia os dados do formulário para a API usando o método fetch()
    const resposta = await fetch('http://127.0.0.1:8000/comentarios/', {
        method: 'POST',
        body: dadosDoFormulario
    });

    // Processa a resposta da API aqui, se necessário

    console.log('Dados enviados com sucesso!');
    location.reload();
    } catch (erro) {
    console.error('Ocorreu um erro ao enviar os dados do formulário:', erro);
    }
});