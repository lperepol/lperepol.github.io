let subjectObject = null;
$(document).ready(function() {
    /*********************************************************************/
    $.ajaxSetup({
        beforeSend: function() {
            // show gif here, eg:
            //$('#loading').show();
            $('body').addClass('loading');
        },
        complete: function() {// hide gif here, eg:
            $('body').removeClass('loading');
        }
    });
    /*********************************************************************/
    console.log('button Click');
    $.ajax({
        'async': false,
        'global': false,
        'url': 'json/KeepMetadata2Json_7.json',
        'dataType': 'json',
        'success': function (data) {
            subjectObject = data;
            console.log(subjectObject);
            getCounts()
        },
        error: function(XMLHttpRequest, textStatus, errorThrown) {
            alert('Status: ' + textStatus); alert('Error: ' + errorThrown);
        }
    });

});

function getCounts() {
    console.log('getCounts');
    //empty Magification- and View and dropdowns
    //display correct values
    orderSet = new Set();
    familySet = new Set();
    genraSet = new Set();
    termSet = new Set();
    console.log('getCounts');
    for (var a in subjectObject) {
        orderSet.add(a)
        console.log(a);  // Orders
        for (var b in subjectObject[a]) {
            console.log('Next Level');
            console.log(b);
        }

    }
}

