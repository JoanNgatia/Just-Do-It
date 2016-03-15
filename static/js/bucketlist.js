(function() {
    'use strict';

    angular
        .module('bucketlist',[
            'bucketlist.routes',
            'bucketlist.account',
            'bucketlist.config'
        ]);

    angular
        .module('bucketlist.routes', ['ngRoute']);

    angular
    .module('bucketlist.config', []);
})();