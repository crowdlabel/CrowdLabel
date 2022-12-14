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
 * The TasksRequest model module.
 * @module model/TasksRequest
 * @version 0.1.0
 */
class TasksRequest {
    /**
     * Constructs a new <code>TasksRequest</code>.
     * @alias module:model/TasksRequest
     */
    constructor() { 
        
        TasksRequest.initialize(this);
    }

    /**
     * Initializes the fields of this object.
     * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
     * Only for internal use.
     */
    static initialize(obj) { 
    }

    /**
     * Constructs a <code>TasksRequest</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/TasksRequest} obj Optional instance to populate.
     * @return {module:model/TasksRequest} The populated <code>TasksRequest</code> instance.
     */
    static constructFromObject(data, obj) {
        if (data) {
            obj = obj || new TasksRequest();

            if (data.hasOwnProperty('name')) {
                obj['name'] = ApiClient.convertToType(data['name'], 'String');
            }
            if (data.hasOwnProperty('credits')) {
                obj['credits'] = ApiClient.convertToType(data['credits'], 'Number');
            }
            if (data.hasOwnProperty('requester')) {
                obj['requester'] = ApiClient.convertToType(data['requester'], 'String');
            }
            if (data.hasOwnProperty('page')) {
                obj['page'] = ApiClient.convertToType(data['page'], 'Number');
            }
            if (data.hasOwnProperty('page_size')) {
                obj['page_size'] = ApiClient.convertToType(data['page_size'], 'Number');
            }
        }
        return obj;
    }

    /**
     * Validates the JSON data with respect to <code>TasksRequest</code>.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @return {boolean} to indicate whether the JSON data is valid with respect to <code>TasksRequest</code>.
     */
    static validateJSON(data) {
        // ensure the json data is a string
        if (data['name'] && !(typeof data['name'] === 'string' || data['name'] instanceof String)) {
            throw new Error("Expected the field `name` to be a primitive type in the JSON string but got " + data['name']);
        }
        // ensure the json data is a string
        if (data['requester'] && !(typeof data['requester'] === 'string' || data['requester'] instanceof String)) {
            throw new Error("Expected the field `requester` to be a primitive type in the JSON string but got " + data['requester']);
        }

        return true;
    }


}



/**
 * @member {String} name
 */
TasksRequest.prototype['name'] = undefined;

/**
 * @member {Number} credits
 */
TasksRequest.prototype['credits'] = undefined;

/**
 * @member {String} requester
 */
TasksRequest.prototype['requester'] = undefined;

/**
 * @member {Number} page
 */
TasksRequest.prototype['page'] = undefined;

/**
 * @member {Number} page_size
 */
TasksRequest.prototype['page_size'] = undefined;






export default TasksRequest;

