// Define an array to store employee data
let employees = [];

// Function to render the employee list
function renderEmployeeList() {
  const tableBody = document.querySelector('tbody');
  tableBody.innerHTML = '';

  employees.forEach((employee, index) => {
    const row = document.createElement('tr');

    const nameCell = document.createElement('td');
    nameCell.textContent = employee.name;
    row.appendChild(nameCell);

    const emailCell = document.createElement('td');
    emailCell.textContent = employee.email;
    row.appendChild(emailCell);

    const phoneCell = document.createElement('td');
    phoneCell.textContent = employee.phone;
    row.appendChild(phoneCell);

    const hireDateCell = document.createElement('td');
    hireDateCell.textContent = employee.hireDate;
    row.appendChild(hireDateCell);

    const actionsCell = document.createElement('td');
    const editButton = document.createElement('button');
    editButton.textContent = 'Edit';
    editButton.classList.add('bg-yellow-500', 'hover:bg-yellow-700', 'text-white', 'font-bold', 'py-1', 'px-2', 'rounded', 'mr-2');
    editButton.addEventListener('click', () => editEmployee(index));
    actionsCell.appendChild(editButton);

    const deleteButton = document.createElement('button');
    deleteButton.textContent = 'Delete';
    deleteButton.classList.add('bg-red-500', 'hover:bg-red-700', 'text-white', 'font-bold', 'py-1', 'px-2', 'rounded');
    deleteButton.addEventListener('click', () => deleteEmployee(index));
    actionsCell.appendChild(deleteButton);

    row.appendChild(actionsCell);
    tableBody.appendChild(row);
  });
}

// Function to add a new employee
function addEmployee(event) {
  event.preventDefault();

  const name = document.getElementById('name').value;
  const email = document.getElementById('email').value;
  const phone = document.getElementById('phone').value;
  const hireDate = document.getElementById('address').value;

  const newEmployee = { name, email, phone, hireDate };
  employees.push(newEmployee);
  renderEmployeeList();

  // Clear the form inputs
  document.getElementById('employeeForm').reset();
}

// Function to edit an existing employee
function editEmployee(index) {
  const employee = employees[index];

  document.getElementById('name').value = employee.name;
  document.getElementById('email').value = employee.email;
  document.getElementById('phone').value = employee.phone;
  document.getElementById('hireDate').value = employee.hireDate;

  // Remove the employee from the array
  employees.splice(index, 1);

  // Update the employee list
  renderEmployeeList();
}

// Function to delete an employee
function deleteEmployee(index) {
  employees.splice(index, 1);
  renderEmployeeList();
}

// Add event listener to the form
const employeeForm = document.getElementById('employeeForm');
employeeForm.addEventListener('submit', addEmployee);

// Render the initial employee list
renderEmployeeList();
