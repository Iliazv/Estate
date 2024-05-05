function openSection(id) {
    const links = document.querySelectorAll('.switch__link')
    const sections = document.querySelectorAll('.container__section')

    for (let i = 1; i < links.length + 1; i++) {
      let link = links[i - 1]
      let section = sections[i - 1]
      if (link.classList.contains('main')) {
        link.classList.remove('main')
        section.classList.remove('activate-section')
      } 
      if (i == id) {
        link.classList.add('main')
        section.classList.add('activate-section')
      }
    }
}