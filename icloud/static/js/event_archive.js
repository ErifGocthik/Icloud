(function remove_archive() {
    $(document).ready(function () {
        let listImageArchive = [];
        let imageIdArchive = null;
        let idPage = document.URL;
        let idArchive = idPage[idPage.length - 1];
        if (document.URL == `http://127.0.0.1:8000/icloud/archive/${idPage[idPage.length - 1]}`) {
            $('.archive_images').mousedown(function (e) {
                if (e.which == 3) {
                    e.target.className.split(' ').forEach(function (item) {
                        if (item.indexOf('img') !== -1) {
                            imageIdArchive = Number(item.split('_')[1]);
                            if (listImageArchive.includes(imageIdArchive) !== true) {
                                listImageArchive.push(Number(item.split('_')[1]));
                                console.clear();
                                console.log(listImageArchive);
                                if (listImageArchive.length != 0) {
                                    $('.list_choose_menu').css({'transform': 'translateX(-3.1vw)'});
                                }
                                $(`.img_${imageIdArchive}_id`).css({'filter': 'brightness(0.5)'});
                            } else if (listImageArchive.includes(imageIdArchive)) {
                                listImageArchive.splice(listImageArchive.indexOf(Number(item.split('_')[1])), 1);
                                console.clear();
                                console.log(listImageArchive);
                                if (listImageArchive.length == 0) {
                                    $('.list_choose_menu').css({'transform': ' translateX(0)'});
                                }
                                $(`.img_${imageIdArchive}_id`).css({'filter': 'brightness(1)'});
                            }
                        }
                    });
                }
            });
            $('.delete_btn_a').mousedown(function (event) {
                this.classList.add("delete_image_block");
                while (listImageArchive.length != 0) {
                    let indexList = listImageArchive[0];
                    $.get(`${idArchive}/remove/${indexList}`,
                        success = function (data) {
                            if (data.successed) {
                                $(`.img_${indexList}_id`).remove();
                            }
                        });
                    listImageArchive.shift();
                }
            });
        }
    });
})();