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
    instance = new DeRegNetRestApi.ParameterSetInfo();
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

  describe('ParameterSetInfo', function() {
    it('should create an instance of ParameterSetInfo', function() {
      // uncomment below and update the code to test ParameterSetInfo
      //var instane = new DeRegNetRestApi.ParameterSetInfo();
      //expect(instance).to.be.a(DeRegNetRestApi.ParameterSetInfo);
    });

    it('should have the property description (base name: "description")', function() {
      // uncomment below and update the code to test the property description
      //var instane = new DeRegNetRestApi.ParameterSetInfo();
      //expect(instance).to.be();
    });

    it('should have the property id (base name: "id")', function() {
      // uncomment below and update the code to test the property id
      //var instane = new DeRegNetRestApi.ParameterSetInfo();
      //expect(instance).to.be();
    });

    it('should have the property setParameters (base name: "set_parameters")', function() {
      // uncomment below and update the code to test the property setParameters
      //var instane = new DeRegNetRestApi.ParameterSetInfo();
      //expect(instance).to.be();
    });

  });

}));
