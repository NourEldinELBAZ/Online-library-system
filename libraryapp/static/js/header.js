function generateLinks(isAdmin) {
    var currentPage = window.location.pathname;
    var links = [];
  
    if (isAdmin) {
        links = [
            { text: 'Home', href: currentPage === '/' ? '#' : '/' },
            { text: 'Available Books', href: currentPage === '/viewbooks/' ? '#' : '/viewbooks/' },
            { text: 'Add Book', href: currentPage === '/addbook/' ? '#' : '/addbook/' },
            { text: 'Log out', href: '/logout/' },
        ];
    } else {
        links = [
            { text: 'Home', href: currentPage === '/' ? '#' : '/' },
            { text: 'Available Books', href: currentPage === '/viewbooks' ? '#' : '/viewbooks' },
            { text: 'Borrowed Books', href: currentPage === '/borrowedbooks' ? '#' : '/borrowedbooks' },
            { text: 'Search', href: currentPage === '/search' ? '#' : '/search' },
            { text: 'Log out', href: '/logout/' },
        ];
    }
  
    return links;
}

  
  // Function to create header with dynamic links
  function createHeader(title, isAdmin) {
    var header = document.createElement('header');
    var h2 = document.createElement('h2');
    h2.className = 'page-name';
    h2.textContent = title || 'Available Books';
    header.appendChild(h2);
  
    var nav = document.createElement('nav');
    var ul = document.createElement('ul');
  
    var links = generateLinks(isAdmin);
  
    links.forEach(function(link) {
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.textContent = link.text;
        a.href = link.href;
        li.appendChild(a);
        ul.appendChild(li);
    });
  
    nav.appendChild(ul);
    header.appendChild(nav);
  
    document.body.appendChild(header);
  }