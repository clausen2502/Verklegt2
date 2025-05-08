
/*Location Filter JavaScript  ---------------------------------------------------------------------------------------------------------------*/
function toggleLocationDropdown() {
    const dropdown = document.getElementById('locationDropdown');
    if (dropdown.style.display === 'none') {
    dropdown.style.display = 'block';
    } else {
        dropdown.style.display = 'none';
    }
}

/*Type Filter JavaScript  ---------------------------------------------------------------------------------------------------------------*/
function toggleTypeDropdown() {
    const typeDropdown = document.getElementById('type-dropdown');
    if (typeDropdown.style.display === 'none' || typeDropdown.style.display === '') {
        typeDropdown.style.display = 'block';
    } else {
        typeDropdown.style.display = 'none';
    }
}



