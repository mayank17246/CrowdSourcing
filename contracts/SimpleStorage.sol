// SPDX-License-Identifier: MIT
pragma solidity ^0.6.0;

//We are creating a simple application that can store information on blockchain for us.

contract SimpleStorage {
    uint256 favoriteNumber;
    //this will get initialized to 0

    //Here we a new type People that has favorite number and a name inside of it.
    struct People {
        uint256 favoriteNumber;
        string name;
    }

    // People public person = People({favoriteNumber : 2, name: "Patrick"});
    People[] public people;

    mapping(string => uint256) public nameToFavNumber;

    function store(uint256 _favoriteNumber) public {
        favoriteNumber = _favoriteNumber;
    }

    //view,pure
    function retrive() public view returns (uint256) {
        return favoriteNumber;
    }

    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({favoriteNumber: _favoriteNumber, name: _name}));
        nameToFavNumber[_name] = _favoriteNumber;
    }
}
