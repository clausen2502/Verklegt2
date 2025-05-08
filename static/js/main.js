/* Location Filter JavaScript ---------------------------------------------------------------------- */
function toggleLocationDropdown() {
    toggleDropdown('locationDropdown');
}

/* Type Filter JavaScript -------------------------------------------------------------------------- */
function toggleTypeDropdown() {
    toggleDropdown('typeDropdown');
}

/* Size Filter JavaScript -------------------------------------------------------------------------- */
function toggleSizeDropdown() {
    toggleDropdown('sizeDropdown');
}

/* Room Filter JavaScript -------------------------------------------------------------------------- */
function toggleRoomDropdown() {
    toggleDropdown('roomDropdown');
}

/* General Dropdown Toggle Function ---------------------------------------------------------------- */
function toggleDropdown(id) {
    const dropdown = document.getElementById(id);
    if (dropdown.style.display === 'none' || dropdown.style.display === '') {
        dropdown.style.display = 'block';
    } else {
        dropdown.style.display = 'none';
    }
}


