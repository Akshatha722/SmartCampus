const complaintForm = document.getElementById("complaintForm");

const complaintList = document.getElementById("complaintList");

let complaints = [];

complaintForm.addEventListener("submit", function(event) {

    event.preventDefault();

    const studentName = document.getElementById("studentName").value;
    const category = document.getElementById("category").value;
    const description = document.getElementById("description").value;

    const complaint = {
        studentName: studentName,
        category: category,
        description: description,
        status: "Pending"
    };

    complaints.push(complaint);

    displayComplaints();

    complaintForm.reset();

});

function displayComplaints() {

    complaintList.innerHTML = "";

    complaints.forEach(function(complaint) {

        const card = document.createElement("div");

        card.className = "complaint-card";

        card.innerHTML = `
            <h3>${complaint.category}</h3>
            <p><strong>Student:</strong> ${complaint.studentName}</p>
            <p><strong>Description:</strong> ${complaint.description}</p>
            <p><strong>Status:</strong> ${complaint.status}</p>
        `;

        complaintList.appendChild(card);

    });

}