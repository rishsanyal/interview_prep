const inputBox = document.getElementById("input-box");
const listContainer = document.getElementById("list-container");

const taskButton = document.getElementById("task-button");
taskButton.addEventListener("click", addTask);

const closeButton = document.getElementById("close");

function addTask() {
    if (inputBox.value === '') {
        alert('You must write something')
    } else {
        let li = document.createElement('li');
        li.innerHTML = inputBox.value;
        listContainer.appendChild(li);

        let span = document.createElement('span');
        span.innerHTML = '\u00d7';
        span.id = 'close';

        li.appendChild(span);

        saveData();
    }

    inputBox.value = '';
}

listContainer.addEventListener("click", removeTask);

function removeTask(e) {
    if (e.target.id === 'close') {
        e.target.parentElement.remove();
    } else {
        e.target.classList.toggle('checked');
    }
    saveData();
}

function saveData() {
    localStorage.setItem('data', listContainer.innerHTML);
}

function showTask() {
    listContainer.innerHTML = localStorage.getItem('data');
}
showTask();