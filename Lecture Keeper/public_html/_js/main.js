function switch_clss(clss, what, toWhat) {
    tmp = document.getElementsByClassName(clss);
    for (var i = tmp.length - 1; i >= 0; i--) {
        tmp[i].setAttribute('class', tmp[0].className.replace(what, toWhat))
    };
}

function show_menu() {
    switch_clss('darken', 'hide', 'show');
    switch_clss('menu', 'hide', 'show');
};

function hide_menu() {
    switch_clss('darken', 'show', 'hide');
    switch_clss('menu', 'show', 'hide');
};


function switch_to_list() {
    switch_clss('lec_card_grid', 'grid', 'list');

    tmp = document.getElementsByClassName('list not_pressed');
    tmp[0].setAttribute('class', 'list');

	tmp = document.getElementsByClassName('grid');
    tmp[0].setAttribute('class', 'grid not_pressed');

    // switch_clss('grid', 'grid', 'grid not_pressed');
    // switch_clss('list not_pressed', 'list not_pressed', 'list');

    // switch_clss('list', 'list', 'list not_pressed');
    // switch_clss('grid not_pressed', 'grid not_pressed', 'grid');

}

function switch_to_grid() {
    switch_clss('lec_card_list', 'list', 'grid');

    tmp = document.getElementsByClassName('grid not_pressed');
    tmp[0].setAttribute('class', 'grid');

	tmp = document.getElementsByClassName('list');
    tmp[0].setAttribute('class', 'list not_pressed');

    // switch_clss('grid', 'grid', 'grid not_pressed');
    // switch_clss('list not_pressed', 'list not_pressed', 'list');

    // switch_clss('list', 'list', 'list not_pressed');
    // switch_clss('grid not_pressed', 'grid not_pressed', 'grid');
}