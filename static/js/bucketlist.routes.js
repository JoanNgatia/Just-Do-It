(function () {
    'use strict';

    angular
        .module('bucketlist.routes')
        .config(config);

    config.$inject = ['$routeProvider'];

    function config($routeProvider) {
        $routeProvider.when('/register', {
            controller: 'RegisterController',
            controllerAs: 'vm',
            templateUrl: 'static/templates/accout.html'
        }).otherwise('/');
    }
})();