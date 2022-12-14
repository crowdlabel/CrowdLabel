/**
 * CrowdLabelAPI
 * API for CrowdLabel
 *
 * The version of the OpenAPI document: 0.1.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 *
 */

(function(root, factory) {
  if (typeof define === 'function' && define.amd) {
    // AMD.
    define(['expect.js', process.cwd()+'/src/index'], factory);
  } else if (typeof module === 'object' && module.exports) {
    // CommonJS-like environments that support module.exports, like Node.
    factory(require('expect.js'), require(process.cwd()+'/src/index'));
  } else {
    // Browser globals (root is window)
    factory(root.expect, root.CrowdLabelApi);
  }
}(this, function(expect, CrowdLabelApi) {
  'use strict';

  var instance;

  beforeEach(function() {
    instance = new CrowdLabelApi.Answer1();
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

  describe('Answer1', function() {
    it('should create an instance of Answer1', function() {
      // uncomment below and update the code to test Answer1
      //var instance = new CrowdLabelApi.Answer1();
      //expect(instance).to.be.a(CrowdLabelApi.Answer1);
    });

    it('should have the property choice (base name: "choice")', function() {
      // uncomment below and update the code to test the property choice
      //var instance = new CrowdLabelApi.Answer1();
      //expect(instance).to.be();
    });

    it('should have the property choices (base name: "choices")', function() {
      // uncomment below and update the code to test the property choices
      //var instance = new CrowdLabelApi.Answer1();
      //expect(instance).to.be();
    });

    it('should have the property ranking (base name: "ranking")', function() {
      // uncomment below and update the code to test the property ranking
      //var instance = new CrowdLabelApi.Answer1();
      //expect(instance).to.be();
    });

    it('should have the property topLeft (base name: "top_left")', function() {
      // uncomment below and update the code to test the property topLeft
      //var instance = new CrowdLabelApi.Answer1();
      //expect(instance).to.be();
    });

    it('should have the property bottomRight (base name: "bottom_right")', function() {
      // uncomment below and update the code to test the property bottomRight
      //var instance = new CrowdLabelApi.Answer1();
      //expect(instance).to.be();
    });

    it('should have the property text (base name: "text")', function() {
      // uncomment below and update the code to test the property text
      //var instance = new CrowdLabelApi.Answer1();
      //expect(instance).to.be();
    });

  });

}));
