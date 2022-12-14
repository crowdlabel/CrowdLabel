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

/**
 * The SingleChoiceAnswer model module.
 * @module model/SingleChoiceAnswer
 * @version 0.1.0
 */
class SingleChoiceAnswer {
    /**
     * Constructs a new <code>SingleChoiceAnswer</code>.
     * @alias module:model/SingleChoiceAnswer
     * @param choice {Number} 
     */
    constructor(choice) { 
        
        SingleChoiceAnswer.initialize(this, choice);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj, choice) { 
        obj['choice'] = choice;
    }

    /**
     * Constructs a <code>SingleChoiceAnswer</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/SingleChoiceAnswer} obj Optional instance to populate.
     * @return {module:model/SingleChoiceAnswer} The populated <code>SingleChoiceAnswer</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new SingleChoiceAnswer();

            if (data.hasOwnProperty('choice')) {
                obj['choice'] = ApiClient.convertToType(data['choice'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>SingleChoiceAnswer</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>SingleChoiceAnswer</code>.
     */
    static validateJSON(data) {
        // check to make sure all required properties are present in the JSON string
        for (const property of SingleChoiceAnswer.RequiredProperties) {
            if (!data[property]) {
                throw new Error("The required field `" + property + "` is not found in the JSON data: " + JSON.stringify(data));
            }
        }

        return true;
    }


}

SingleChoiceAnswer.RequiredProperties = ["choice"];

/**
 * @member {Number} choice
 */
SingleChoiceAnswer.prototype['choice'] = undefined;






export default SingleChoiceAnswer;

