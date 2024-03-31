{
    document.addEventListener('DOMContentLoaded', function() {
        const navLinks = document.querySelectorAll('.nav-link');
        const userIcon = document.querySelector('.user-icon');
        const userContent = document.getElementById('user');
    
        navLinks.forEach(function(navLink) {
          navLink.addEventListener('click', function(event) {
            const target = event.target.getAttribute('href');
            document.querySelectorAll('.content > div').forEach(function(contentDiv) {
                console.log(target)
              contentDiv.style.display = 'none';
            });
            userContent.style.display = 'none'; // Hide user content when any nav link is clicked
            document.querySelector(target).style.display = 'block';
          });
        });
    
        // Toggle user content when user icon is clicked
        userIcon.addEventListener('click', function() {
            document.querySelectorAll('.nav-link').forEach(function(navLink) {
                document.querySelectorAll('.content > div').forEach(function(contentDiv) {      
                    contentDiv.style.display = 'none';
                });
            });
            userContent.style.display = userContent.style.display === 'none' ? 'block' : 'none';
        });
    });
}