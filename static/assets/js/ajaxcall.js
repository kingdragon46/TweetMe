// function getSTBbyID() {
//     var stdData = $('#sltSTB').val();
//     _success = function (res) {
//         // console.log(res);
//         var data = res[0].fields;
//         console.log(data.DOP)
//         $('#stbSNo').val(data.serial_number);
//         $('#stbDOP').val(data.DOP);
//         $('#stbIssueDate').val(data.issue_date);
//         $('#stbModel').val(data.model_number);
//         $('#stbType').val(data.Type);
//         console.log(data);
//         $('#stbRemark').val(data.remark);
//         $('#stbBox').val(data.box_type);
//         $('#stbStatus').val(data.status);
//         console.log(data);
//     }
//     _error = function (error) {
//         console.log(error);

//     }


//     callAjaxGet('/getSTBbyID/' + stdData + '/', '', _success, _error, false, '');