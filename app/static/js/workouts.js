{   
    document.addEventListener('DOMContentLoaded', function() {
        /* CODE TO CALL API AND GET EXERCISES
        fetch('http://127.0.0.1:5000/callExercisesAPI') // Retrieve and Save exercises'
            .then(response => response.json())
            .then(data => {
              
              console.log('Data was saved successfully');
              
            })
            .catch(error => console.error('Error:', error));
        */
        // Fetch GIF URL when "Workouts" tab is clicked
        function get_gif_url(exercise_name) {
            var cleared_exercise_name = exercise_name.replace(' ','_')
              fetch(`http://127.0.0.1:5000/workouts/${cleared_exercise_name}/get_gif_url`) // Assuming the Flask route is '/get_gif_url'
                .then(response => response.json())
                .then(data => {
                  const gifUrl = data.gifURL;
                  console.log('GIF URL',data.gifURL);
                  return gifUrl;
                  /*
                  fetch(gifUrl, { 
                    headers: { 'X-RapidAPI-Key' : 'c8f7c942c6msh71c58f5865ee5c7p188819jsn6bb86afec4f2',
                               'X-RapidAPI-Host' : 'exercisedb.p.rapidapi.com',
                               
                            }, 
                    mode: 'no-cors'
                  })
                    .then(response => response.blob())
                    .then(blob => {
                        const objectURL = URL.createObjectURL(blob);
                        return objectURL;
                    })
                    .catch(error => {
                        console.error('There was a problem with the fetch operation:', error);
                    });*/
                })
                .catch(error => console.error('Error:', error));
            
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

                    //var gifurl = document.createElement("img");
                    //gifurl.src = get_gif_url(exercise.name);

                    //rightdiv.appendChild(gifurl);

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
                    })
                    .catch(error => console.error('Error: ', error));
            
        }
        
        document.querySelector('a[href="#workouts"]').addEventListener('click', function() {
            show_exercises();
        });
    });
    
}