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

import ApiClient from '../ApiClient';
import Answer from './Answer';

/**
 * The MultiChoiceQuestion model module.
 * @module model/MultiChoiceQuestion
 * @version 0.1.0
 */
class MultiChoiceQuestion {
    /**
     * Constructs a new <code>MultiChoiceQuestion</code>.
     * @alias module:model/MultiChoiceQuestion
     * @param questionId {Number} 
     * @param prompt {String} 
     * @param options {Array.<String>} 
     */
    constructor(questionId, prompt, options) { 
        
        MultiChoiceQuestion.initialize(this, questionId, prompt, options);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, questionId, prompt, options) { 
        obj['question_id'] = questionId;
        obj['prompt'] = prompt;
        obj['options'] = options;
    }

    /**
     * Constructs a <code>MultiChoiceQuestion</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/MultiChoiceQuestion} obj Optional instance to populate.
     * @return {module:model/MultiChoiceQuestion} The populated <code>MultiChoiceQuestion</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new MultiChoiceQuestion();

            if (data.hasOwnProperty('question_id')) {
                obj['question_id'] = ApiClient.convertToType(data['question_id'], 'Number');
            }
            if (data.hasOwnProperty('question_type')) {
                obj['question_type'] = ApiClient.convertToType(data['question_type'], 'String');
            }
            if (data.hasOwnProperty('prompt')) {
                obj['prompt'] = ApiClient.convertToType(data['prompt'], 'String');
            }
            if (data.hasOwnProperty('resource')) {
                obj['resource'] = ApiClient.convertToType(data['resource'], 'String');
            }
            if (data.hasOwnProperty('answers')) {
                obj['answers'] = ApiClient.convertToType(data['answers'], [Answer]);
            }
            if (data.hasOwnProperty('options')) {
                obj['options'] = ApiClient.convertToType(data['options'], ['String']);
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>MultiChoiceQuestion</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>MultiChoiceQuestion</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of MultiChoiceQuestion.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }
        // ensure the json data is a string
        if (data['question_type'] && !(typeof data['question_type'] === 'string' || data['question_type'] instanceof String)) {
            throw new Error("Expected the field `question_type` to be a primitive type in the JSON string but got " + data['question_type']);
        }
        // ensure the json data is a string
        if (data['prompt'] && !(typeof data['prompt'] === 'string' || data['prompt'] instanceof String)) {
            throw new Error("Expected the field `prompt` to be a primitive type in the JSON string but got " + data['prompt']);
        }
        // ensure the json data is a string
        if (data['resource'] && !(typeof data['resource'] === 'string' || data['resource'] instanceof String)) {
            throw new Error("Expected the field `resource` to be a primitive type in the JSON string but got " + data['resource']);
        }
        if (data['answers']) { // data not null
            // ensure the json data is an array
            if (!Array.isArray(data['answers'])) {
                throw new Error("Expected the field `answers` to be an array in the JSON data but got " + data['answers']);
            }
            // validate the optional field `answers` (array)
            for (const item of data['answers']) {
                Answer.validateJsonObject(item);
            };
        }
        // ensure the json data is an array
        if (!Array.isArray(data['options'])) {
            throw new Error("Expected the field `options` to be an array in the JSON data but got " + data['options']);
        }

        return true;
    }


}

MultiChoiceQuestion.RequiredProperties = ["question_id", "prompt", "options"];

/**
 * @member {Number} question_id
 */
MultiChoiceQuestion.prototype['question_id'] = undefined;

/**
 * @member {String} question_type
 * @default 'multi_choice'
 */
MultiChoiceQuestion.prototype['question_type'] = 'multi_choice';

/**
 * @member {String} prompt
 */
MultiChoiceQuestion.prototype['prompt'] = undefined;

/**
 * @member {String} resource
 */
MultiChoiceQuestion.prototype['resource'] = undefined;

/**
 * @member {Array.<module:model/Answer>} answers
 */
MultiChoiceQuestion.prototype['answers'] = undefined;

/**
 * @member {Array.<String>} options
 */
MultiChoiceQuestion.prototype['options'] = undefined;






export default MultiChoiceQuestion;

