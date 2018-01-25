/**
 * DeRegNet REST API
 * DeRegNet REST API 
 *
 * OpenAPI spec version: 0.0.1
 * Contact: deregnet@informatik.uni-tuebingen.de
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', '../../src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require('../../src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.DeRegNetRestApi);
  }
}(this, function(expect, DeRegNetRestApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new DeRegNetRestApi.ScoreInfo();
  });

  var getProperty = function(object, getter, property) {
    // Use getter method if present; otherwise, get the property directly.
    if (typeof object[getter] === 'function')
      return object[getter]();
    else
      return object[property];
  }

  var setProperty = function(object, setter, property, value) {
    // Use setter method if present; otherwise, set the property directly.
    if (typeof object[setter] === 'function')
      object[setter](value);
    else
      object[property] = value;
  }

  describe('ScoreInfo', function() {
    it('should create an instance of ScoreInfo', function() {
      // uncomment below and update the code to test ScoreInfo
      //var instane = new DeRegNetRestApi.ScoreInfo();
      //expect(instance).to.be.a(DeRegNetRestApi.ScoreInfo);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instane = new DeRegNetRestApi.ScoreInfo();
      //expect(instance).to.be();
    });

    it('should have the property size (base name: "size")', function() {
      // uncomment below and update the code to test the property size
      //var instane = new DeRegNetRestApi.ScoreInfo();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instane = new DeRegNetRestApi.ScoreInfo();
      //expect(instance).to.be();
    });

    it('should have the property timeOfUpload (base name: "time_of_upload")', function() {
      // uncomment below and update the code to test the property timeOfUpload
      //var instane = new DeRegNetRestApi.ScoreInfo();
      //expect(instance).to.be();
    });

  });

}));
