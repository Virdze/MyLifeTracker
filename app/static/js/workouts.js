{   
    document.addEventListener('DOMContentLoaded', function() {
        // Fetch GIF URL when "Workouts" tab is clicked
        function get_gif_url() {
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
        }

        function create_exercise_row(exercise) {
            var row = document.createElement("div")
            row.className = "row";
            
                var leftdiv = document.createElement("div");
                leftdiv.className = "col-md-8";

                    var heading = document.createElement("h3");
                    heading.textContent = exercise.name;

                    var description = document.createElement("p");
                    description.textContent = exercise.instructions;

                    leftdiv.appendChild(heading);
                    leftdiv.appendChild(description);
            
                var rightdiv = document.createElement("div");
                rightdiv.className = "col-md-4";

                    var gifurl = document.createElement("img");
                    gifurl.src = exercise.gifURL;

                    rightdiv.appendChild(gifurl);

            row.appendChild(leftdiv);
            row.appendChild(rightdiv);

            return row;
        }

        function show_exercises(){            
                fetch('http://127.0.0.1:5000/workouts/getExercises')
                    .then(response => response.json())
                    .then(data => {
                        const exercises = data;
                        console.log('Exercises',data);
                        
                        //get container by ID and reset the content
                        var workoutsContainer = document.getElementById("workoutsContainer");
                        workoutsContainer.innerHTML = "";

                        //Create each row
                        exercises.forEach(function(exercise){
                            var exerciseRow = create_exercise_row(exercise);
                            workoutsContainer.appendChild(exerciseRow);
                        });
                    });
            
        }
        
        document.querySelector('a[href="#workouts"]').addEventListener('click', function() {
            show_exercises();
        });
    });
    
}