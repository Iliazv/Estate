const loginButton = document.getElementById('login-button')
const overlayButton = document.getElementById('overlay')
const crossButton = document.getElementById('cross-button')
const crossButtonReg = document.getElementById('cross-button-reg')
const registerButton = document.getElementById('register-button')
const loginButtonSwitch = document.getElementById('login-button-switch')


function openModal() {
    let modal = document.querySelector('.modal')
    let overlay = document.querySelector('.overlay')
    if (modal.classList.contains('hidden')) {
        modal.classList.remove('hidden')
        overlay.classList.remove('hidden')
        modal.classList.add('opened')
        overlay.classList.add('opened')
    }
}

function closeModal() {
    let modal = document.querySelector('.modal')
    let modal_reg = document.querySelector('.modalreg')
    let overlay = document.querySelector('.overlay')
    if (modal.classList.contains('opened')) {
        modal.classList.remove('opened')
        overlay.classList.remove('opened')
        modal.classList.add('hidden')
        overlay.classList.add('hidden')
    }
    if (modal_reg.classList.contains('opened')) {
        modal_reg.classList.remove('opened')
        overlay.classList.remove('opened')
        modal_reg.classList.add('hidden')
        overlay.classList.add('hidden')
    }
}

function switchModal() {
    let modal = document.querySelector('.modal')
    let modal_reg = document.querySelector('.modalreg')
    console.log('start')
    if (modal.classList.contains('opened')) {
        modal.classList.remove('opened')
        modal.classList.add('hidden')
        modal_reg.classList.remove('hidden')
        modal_reg.classList.add('opened')
        console.log('end')
    } else {
        modal.classList.remove('hidden')
        modal.classList.add('opened')
        modal_reg.classList.remove('opened')
        modal_reg.classList.add('hidden')
    }
}


loginButton.addEventListener('click', function(e) {
    openModal()
})

overlayButton.addEventListener('click', function(e) {
    closeModal()
})

crossButton.addEventListener('click', function(e) {
    closeModal()
})

crossButtonReg.addEventListener('click', function(e) {
    closeModal()
})

registerButton.addEventListener('click', function(e) {
    switchModal()
})

loginButtonSwitch.addEventListener('click', function(e) {
    switchModal()
})