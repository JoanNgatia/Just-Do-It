(function() {
    'use strict';

    angular
        .module('bucketlist.account.controllers')
        .controller('RegisterController', RegisterController);

    RegisterController.$inject = ['$location', '$scope', 'Account'];

    function RegisterController($location, $scope, Account) {
        var vm = this;

        vm.register = register;

        function register() {
            Account.register(vm.username, vm.password);
        }
    }
}) ();