function fetchQuestions() {
    const difficulty = document.getElementById('difficulty').value;
    const tags = document.getElementById('tags').value;

    fetch(`/filter?difficulty=${difficulty}&tags=${tags}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('results');
            resultsDiv.innerHTML = ''; 
            data.forEach(question => {
                const p = document.createElement('p');
                p.textContent = `Q: ${question.question} - A: ${question.answer}`;
                resultsDiv.appendChild(p);
            });
        })
        .catch(error => console.error('Error:', error));
}
