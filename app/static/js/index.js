{
    document.addEventListener('DOMContentLoaded', function() {
        // Fetch GIF URL when "Workouts" tab is clicked
        const exercise_name = 'archer pull up'
        
        document.querySelector('a[href="#workouts"]').addEventListener('click', function() {
          fetch("http://127.0.0.1:5000/workouts/get_gif_url") // Assuming the Flask route is '/get_gif_url'
            .then(response => response.json())
            .then(data => {
              const gifUrl = data.gifURL;
              document.getElementById('workout-gif').src = gifUrl;
            })
            .catch(error => console.error('Error:', error));
        });
            

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