(function () {
    'use strict';

    angular
        .module('bucketlist.account', [
            'bucketlist.account.controllers',
            'bucketlist.account.services'
        ]);

    angular
        .module('bucketlist.account.controllers', []);

    angular
        .module('bucketlist.account.services', ['ngCookies']);
}) ();