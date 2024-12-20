// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {
    struct Student {
        string name;
        uint256 age;
        string class;
        uint256 rollNumber;
    }

    Student[] public students;

    event StudentAdded(string name, uint256 rollNumber);
    event FallbackCalled(address sender, uint256 amount, string message);

    function addStudent(string memory _name, uint256 _age, string memory _class, uint256 _rollNumber) public {
        Student memory newStudent = Student({name: _name, age: _age, class: _class, rollNumber: _rollNumber});

        students.push(newStudent);

        emit StudentAdded(_name, _rollNumber);
    }

    function getTotalStudents() public view returns (uint256) {
        return students.length;
    }

    function getStudent(uint256 index) public view returns (string memory, uint256, string memory, uint256) {
        require(index < students.length, "Invalid Index");
        Student memory student = students[index];
        return (student.name, student.age, student.class, student.rollNumber);
    }

    fallback() external payable {
        emit FallbackCalled(msg.sender, msg.value, "Thank you for Sending Ether");
    }

    receive() external payable {
    }

    function getContractBalance() public view returns (uint256) {
        return address(this).balance;
    }
}