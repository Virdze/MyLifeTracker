{
    document.addEventListener('DOMContentLoaded', function() {
        // Fetch GIF URL when "Workouts" tab is clicked
        const exercise_name = 'archer_pull_up'
        
        document.querySelector('a[href="#workouts"]').addEventListener('click', function() {
          fetch('http://127.0.0.1:5000/workouts/archer_pull_up/get_gif_url') // Assuming the Flask route is '/get_gif_url'
            .then(response => response.json())
            .then(data => {
              const gifUrl = data.gifURL;
              console.log('GIF URL',data);
              document.getElementById('workout-gif').src = gifUrl;
            })
            .catch(error => console.error('Error:', error));
        });
    });
}