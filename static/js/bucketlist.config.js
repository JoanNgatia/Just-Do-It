(function () {
    'use strict';

    angular
        .module('bucketlist.config')
        .config(config);

    config.$inject = ['$locationProvider'];

    function config(4locationProvider) {
        $locationProvider.html5Mode(true);
        $locationProvider.hashPrefix('!';)
    }
})();