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
    instance = new CrowdLabelApi.MultiChoiceQuestion();
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

  describe('MultiChoiceQuestion', function() {
    it('should create an instance of MultiChoiceQuestion', function() {
      // uncomment below and update the code to test MultiChoiceQuestion
      //var instance = new CrowdLabelApi.MultiChoiceQuestion();
      //expect(instance).to.be.a(CrowdLabelApi.MultiChoiceQuestion);
    });

    it('should have the property questionId (base name: "question_id")', function() {
      // uncomment below and update the code to test the property questionId
      //var instance = new CrowdLabelApi.MultiChoiceQuestion();
      //expect(instance).to.be();
    });

    it('should have the property questionType (base name: "question_type")', function() {
      // uncomment below and update the code to test the property questionType
      //var instance = new CrowdLabelApi.MultiChoiceQuestion();
      //expect(instance).to.be();
    });

    it('should have the property prompt (base name: "prompt")', function() {
      // uncomment below and update the code to test the property prompt
      //var instance = new CrowdLabelApi.MultiChoiceQuestion();
      //expect(instance).to.be();
    });

    it('should have the property resource (base name: "resource")', function() {
      // uncomment below and update the code to test the property resource
      //var instance = new CrowdLabelApi.MultiChoiceQuestion();
      //expect(instance).to.be();
    });

    it('should have the property answers (base name: "answers")', function() {
      // uncomment below and update the code to test the property answers
      //var instance = new CrowdLabelApi.MultiChoiceQuestion();
      //expect(instance).to.be();
    });

    it('should have the property options (base name: "options")', function() {
      // uncomment below and update the code to test the property options
      //var instance = new CrowdLabelApi.MultiChoiceQuestion();
      //expect(instance).to.be();
    });

  });

}));
