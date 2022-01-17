(function(win,doc){
    'use strict';

    // Verifica se o usuário está certo de que deseja deletar o dado.
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(i=0; i < btnDel.length; i++){
            btnDel[i].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar este dado?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
            
        }

    }

    // Ajax do form
    if(doc.querySelector('#form')){
        let form=doc.querySelector('#form')
    }
})(window,document);