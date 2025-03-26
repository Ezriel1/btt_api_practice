// Events are things that happening like a mouse click or button click or refresh, a listern is waiting for an event to happen defined in the arguments DOMcontentloaded just waits for the content to load

document.addEventListener("DOMContentLoaded", function(){

    // will be able to get elements by Id like taskForm, the event listner will listen to that particular element which is us hitting the submit button, 
    // async means it's asychronist which means the function will wait until the respons that is in await is fulfilled, 
    //function will make a promise and fulfill or not and then act accordingly.
    document.getElementById("taskForm").addEventListener("submit", async function(event){
        event.preventDefault()
        // this is needed to prevent the default action of refreshing from happeing

        const description = document.getElementById("description").value

        const taskData = {
            description: description,
            isComplete: false
        }

        const response = await fetch("http://localhost:8000/task",
        
            {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                    "Accept": "application/json"
                },
                body: JSON.stringify(taskData)
                //converting the object to JSON

            }
        )
        // fetch allows us to make a call to an api and then get data, await is where our a sync promise is, we want to wait for this promise to be fulfilled so it doesn't move
        // to the next line of code.

        await response.json()

        console.log(response.json)
    })

})
