
document.querySelector('#task_{{ task.id }}').addEventListener('change', function() {
    // Get the task ID from the checkbox ID
    var task_id = this.id.split('_')[1];
    
    // Send an AJAX request to the Django view function with the updated task data
    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/complete_task/' + task_id + '/');
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onload = function() {
        if (xhr.status === 200) {
            // Update the task data on the page
            var response = JSON.parse(xhr.responseText);
            var completed = response.completed;
            if (completed) {
                document.querySelector('#task_' + task_id).setAttribute('checked', 'checked');
            } else {
                document.querySelector('#task_' + task_id).removeAttribute('checked');
            }
        }
    };
    xhr.send(JSON.stringify({'completed': this.checked,'task_id': task_id}));
});

