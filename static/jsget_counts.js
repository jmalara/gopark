angular.module('get_counts', [])
.controller('car_counts', function($scope, $http) {
    $http.get('http://gpy.io/apizone').
        then(function(response) {
            $scope.car_counts = response.data;
        });
});
