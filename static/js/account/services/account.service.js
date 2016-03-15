(function(){
    'use strict';

    angular
        .module('bucketlist.account.services')
        .factory('Account', Account);

    Account.$inject = ['$cookies', '$http'];

    function Account($cookies, $http) {
        var Account = {
            register: register
        };

        return Account;

        function register(username, password) {
            return $http.post('/api/v1/accounts/', {
                username: username,
                password: password,
                email: email
            });
        }
    }

})();