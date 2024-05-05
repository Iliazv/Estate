const accountButton = document.getElementById('account-button')
const accountBlock = document.querySelector('.account')


accountButton.addEventListener('click', () => {
    if (accountBlock.classList.contains('hidden')) {
        accountBlock.classList.remove('hidden')
        accountBlock.classList.add('opened')
    } else {
        accountBlock.classList.remove('opened')
        accountBlock.classList.add('hidden')
    }
})