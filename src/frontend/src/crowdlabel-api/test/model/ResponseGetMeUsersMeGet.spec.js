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
    instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
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

  describe('ResponseGetMeUsersMeGet', function() {
    it('should create an instance of ResponseGetMeUsersMeGet', function() {
      // uncomment below and update the code to test ResponseGetMeUsersMeGet
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be.a(CrowdLabelApi.ResponseGetMeUsersMeGet);
    });

    it('should have the property userType (base name: "user_type")', function() {
      // uncomment below and update the code to test the property userType
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property email (base name: "email")', function() {
      // uncomment below and update the code to test the property email
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property username (base name: "username")', function() {
      // uncomment below and update the code to test the property username
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property credits (base name: "credits")', function() {
      // uncomment below and update the code to test the property credits
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property dateCreated (base name: "date_created")', function() {
      // uncomment below and update the code to test the property dateCreated
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property passwordHashed (base name: "password_hashed")', function() {
      // uncomment below and update the code to test the property passwordHashed
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property tasksRequested (base name: "tasks_requested")', function() {
      // uncomment below and update the code to test the property tasksRequested
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property tested (base name: "tested")', function() {
      // uncomment below and update the code to test the property tested
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property tasksClaimed (base name: "tasks_claimed")', function() {
      // uncomment below and update the code to test the property tasksClaimed
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

    it('should have the property tasksCompleted (base name: "tasks_completed")', function() {
      // uncomment below and update the code to test the property tasksCompleted
      //var instance = new CrowdLabelApi.ResponseGetMeUsersMeGet();
      //expect(instance).to.be();
    });

  });

}));
