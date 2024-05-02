document.addEventListener("DOMContentLoaded", function() {
    const addButton = document.getElementById("addButton");
    const employeeTableBody = document.getElementById("employeeTableBody");

    // Sample data for testing
    let employees = [
        { id: 1, firstName: "John", lastName: "Doe", email: "john@example.com", salary: 50000, date: "2024-05-01" },
        { id: 2, firstName: "Jane", lastName: "Smith", email: "jane@example.com", salary: 60000, date: "2024-05-01" }
    ];

    // Function to render table rows
    function renderTable() {
        employeeTableBody.innerHTML = "";
        employees.forEach((employee, index) => {
            const row = `
                <tr>
                    <td>${index + 1}</td>
                    <td>${employee.firstName}</td>
                    <td>${employee.lastName}</td>
                    <td>${employee.email}</td>
                    <td>${employee.salary}</td>
                    <td>${employee.date}</td>
                    <td>
                        <button onclick="editEmployee(${employee.id})">Edit</button>
                        <button onclick="deleteEmployee(${employee.id})">Delete</button>
                    </td>
                </tr>
            `;
            employeeTableBody.innerHTML += row;
        });
    }

    // Function to add employee
    function addEmployee() {
        // You can implement code to get input values and add a new employee here
        // For simplicity, I'm adding a sample employee
        const newEmployee = { id: employees.length + 1, firstName: "New", lastName: "Employee", email: "new@example.com", salary: 40000, date: "2024-05-02" };
        employees.push(newEmployee);
        renderTable();
    }

    // Function to edit employee
    function editEmployee(id) {
        console.log("Editing employee with ID:", id);
    }

    // Function to delete employee
    function deleteEmployee(id) {
        employees = employees.filter(employee => employee.id !== id);
        renderTable();
    }

    // Initial rendering of the table
    renderTable();

    // Event listener for add button
    addButton.addEventListener("click", addEmployee);
});