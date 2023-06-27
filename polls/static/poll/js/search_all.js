$(window).on('load', function() {
    $.ajax({
        type: 'get',
        url: "../map_convert/",
        dataType: 'json',
        success: function(data) {
            for (var i=0; i<data.jrent.length; i++) {
                $('#main_middle_search_complete').append('');

                data.jrent[i].bdnm;
                data.jrent[i].gunm + ' ' + data.jrent[i].dongnm + ' ' + data.jrent[i].bn + '-' + data.jrent[i].sbn);
            }

            for (var i=0; i<data.real.length; i++) {
                data.real[i].bdnm;
                data.real[i].gunm + ' ' + data.real[i].dongnm + ' ' + data.real[i].bn + '-' + data.real[i].sbn);
            }

        },
        error: function() {
            console.log('에러')
        }
    });
});