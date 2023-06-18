(function remove() {
    $(document).ready(function() {
        if( document.URL == 'http://127.0.0.1:8000/icloud/') {
            let listImage = [];
            let listArchive = [];
            let allListArchives = document.getElementsByClassName('archive_choose');
            let archiveId = null;
            let imageId = null;
            let archiveInfo = [];
            let imageContain = {};
            $('.image_block').mousedown(function (e) {
                if (e.which == 3) {
                    e.target.className.split(' ').forEach(function (item) {
                        if (item.indexOf('img') !== -1) {
                            imageId = Number(item.split('_')[1]);
                            if (listImage.includes(imageId) !== true) {
                                listImage.push(Number(item.split('_')[1]));
                                if (listImage.length != 0) {
                                    $('.list_choose_menu').css({'transform': 'translateX(-3.1vw)'});
                                }
                                $(`.img_${imageId}_id`).css({'filter': 'brightness(0.5)'});
                            } else if (listImage.includes(imageId)) {
                                listImage.splice(listImage.indexOf(Number(item.split('_')[1])), 1);
                                if (listImage.length == 0) {
                                    $('.list_choose_menu').css({'transform': 'translateX(0)'});
                                }
                                $(`.img_${imageId}_id`).css({'filter': 'brightness(1)'});
                            }
                        }
                    });
                }
            });//f
            $('.delete_btn').mousedown(function (event) {
                this.classList.add("delete_image_block");
                while (listImage.length != 0) {
                    let indexList = listImage[0];
                    $.get(`delete/${indexList}`,
                        success = function (data) {
                            if (data.successed) {
                                $(`.img_${indexList}_id`).remove();
                            }
                        });
                    listImage.shift();
                }
            });
            $('.change_btn').mousedown(function (event) {
                $('.change_window').css({'z-index': '100',
                                        'visibility': 'visible'});
                $('.close_btn').css({'z-index': '101',
                                    'visibility': 'visible'});
                $('header').css({'transform': 'translateX(-5vw)'});
                $('.list_choose_menu').css({'transform': 'translateX(5vw)'});
                for(let i = 0; i < listImage.length; i++) {
                    for(let j = 0; j < allListArchives.length; j++) {
                        $.get(`${allListArchives[j].className.split(' ')[1].split('_')[1]}/add/${listImage[i]}`,
                            success = function (data) {
                                if (data.ifResult) {
                                    $(`.arc_${allListArchives[j].className.split(' ')[1].split('_')[1]}_id`).css({'filter': 'brightness(0.5)'});
                                    listArchive.push(Number(allListArchives[j].className.split(' ')[1].split('_')[1]));
                                }
                            });
                    }
                }
            });
            $('.archive_choose').mousedown(function (e) {
                e.target.className.split(' ').forEach(function (item) {
                    if (item.indexOf('arc') !== -1) {
                        archiveId = Number(item.split('_')[1]);
                    }
                });
                if (e.which == 1) {
                    for (let i = 0; i < listImage.length; i++) {
                        if (listArchive.includes(archiveId) === false) {
                            listArchive.push(archiveId);
                            $.get(`${archiveId}/movein/${listImage[i]}`);
                            $(`.arc_${archiveId}_id`).css({'filter': 'brightness(0.5)'});
                        } else if (listArchive.includes(archiveId) === true) {
                            // listArchive.splice(listArchive.indexOf(archiveId), 1);
                            // $.get(`${archiveId}/moveout/${imageId}`);
                            // $(`.arc_${archiveId}_id`).css({'filter': 'brightness(1)'});
                        }
                    }
                } else if (e.which == 3) {
                    for (let i = 0; i < listImage.length; i++) {
                        if (listArchive.includes(archiveId) === false) {
                            // listArchive.push(archiveId);
                            // $.get(`${archiveId}/movein/${imageId}`);
                            // $(`.arc_${archiveId}_id`).css({'filter': 'brightness(0.5)'});
                        } else if (listArchive.includes(archiveId) === true) {
                            listArchive.splice(listArchive.indexOf(archiveId), 1);
                            $.get(`${archiveId}/moveout/${listImage[i]}`);
                            $(`.arc_${archiveId}_id`).css({'filter': 'brightness(1)'});
                        }
                    }
                }
            });
            $('.close_btn').mousedown(function (e) {
                $('.change_window').css({'z-index': '-98',
                    'visibility': 'hidden'});
                $('.close_btn').css({'z-index': '-97',
                    'visibility': 'hidden'});
                $('header').css({'transform': 'translateX(0)'});
                $('.list_choose_menu').css({'transform': 'translateX(-3.1vw)'});
                for (let i = 0; i < allListArchives.length; i++) {
                    console.log(`.arc_${allListArchives[i].className.split(' ')[1].split('_')[1]}_id`);
                    $(`.arc_${allListArchives[i].className.split(' ')[1].split('_')[1]}_id`).css({'filter': 'brightness(1)'});
                    listArchive.splice(listArchive.indexOf(listArchive[0]), 1);
                }
            });
        }
    });
})();