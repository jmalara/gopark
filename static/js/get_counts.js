▽
angular.module('get_counts', [])
.controller('car_counts', function($scope, $http) {
  $scope.getData = function(){
    $http.get('http://gpy.io/apizone').
        then(function(response) {
            $scope.car_counts = response.data;
        });
  };

  // Run function every second
  setInterval($scope.getData, 1000);
});