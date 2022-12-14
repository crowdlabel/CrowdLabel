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


import ApiClient from "../ApiClient";
import ErrorResponse from '../model/ErrorResponse';
import HTTPValidationError from '../model/HTTPValidationError';
import Task from '../model/Task';
import TasksRequest from '../model/TasksRequest';
import TasksResponse from '../model/TasksResponse';

/**
* Tasks service.
* @module api/TasksApi
* @version 0.1.0
*/
export default class TasksApi {

    /**
    * Constructs a new TasksApi. 
    * @alias module:api/TasksApi
    * @class
    * @param {module:ApiClient} [apiClient] Optional API client implementation to use,
    * default to {@link module:ApiClient#instance} if unspecified.
    */
    constructor(apiClient) {
        this.apiClient = apiClient || ApiClient.instance;
    }


    /**
     * Callback function to receive the result of the claimTaskTasksTaskIdClaimPost operation.
     * @callback module:api/TasksApi~claimTaskTasksTaskIdClaimPostCallback
     * @param {String} error Error message, if any.
     * @param {module:model/Task} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Claim Task
     * @param {Number} taskId 
     * @param {module:api/TasksApi~claimTaskTasksTaskIdClaimPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/Task}
     */
    claimTaskTasksTaskIdClaimPost(taskId, callback) {
      let postBody = null;
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling claimTaskTasksTaskIdClaimPost");
      }

      let pathParams = {
        'task_id': taskId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2PasswordBearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Task;
      return this.apiClient.callApi(
        '/tasks/{task_id}/claim', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the deleteTaskTasksTaskIdDelete operation.
     * @callback module:api/TasksApi~deleteTaskTasksTaskIdDeleteCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Delete Task
     * @param {Number} taskId 
     * @param {module:api/TasksApi~deleteTaskTasksTaskIdDeleteCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    deleteTaskTasksTaskIdDelete(taskId, callback) {
      let postBody = null;
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling deleteTaskTasksTaskIdDelete");
      }

      let pathParams = {
        'task_id': taskId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2PasswordBearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tasks/{task_id}', 'DELETE',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the downloadTaskResultsTasksTaskIdDownloadGet operation.
     * @callback module:api/TasksApi~downloadTaskResultsTasksTaskIdDownloadGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Download Task Results
     * @param {Number} taskId 
     * @param {module:api/TasksApi~downloadTaskResultsTasksTaskIdDownloadGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    downloadTaskResultsTasksTaskIdDownloadGet(taskId, callback) {
      let postBody = null;
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling downloadTaskResultsTasksTaskIdDownloadGet");
      }

      let pathParams = {
        'task_id': taskId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2PasswordBearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tasks/{task_id}/download', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the editTaskTasksTaskIdPatch operation.
     * @callback module:api/TasksApi~editTaskTasksTaskIdPatchCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Edit Task
     * @param {Number} taskId 
     * @param {Object} opts Optional parameters
     * @param {Array.<Object>} opts.requestBody 
     * @param {module:api/TasksApi~editTaskTasksTaskIdPatchCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    editTaskTasksTaskIdPatch(taskId, opts, callback) {
      opts = opts || {};
      let postBody = opts['requestBody'];
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling editTaskTasksTaskIdPatch");
      }

      let pathParams = {
        'task_id': taskId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = [];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tasks/{task_id}', 'PATCH',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTaskTasksTaskIdGet operation.
     * @callback module:api/TasksApi~getTaskTasksTaskIdGetCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Task
     * @param {Number} taskId 
     * @param {module:api/TasksApi~getTaskTasksTaskIdGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    getTaskTasksTaskIdGet(taskId, callback) {
      let postBody = null;
      // verify the required parameter 'taskId' is set
      if (taskId === undefined || taskId === null) {
        throw new Error("Missing the required parameter 'taskId' when calling getTaskTasksTaskIdGet");
      }

      let pathParams = {
        'task_id': taskId
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2PasswordBearer'];
      let contentTypes = [];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tasks/{task_id}', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the getTasksTasksGet operation.
     * @callback module:api/TasksApi~getTasksTasksGetCallback
     * @param {String} error Error message, if any.
     * @param {module:model/TasksResponse} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Get Tasks
     * Task search
     * @param {module:model/TasksRequest} tasksRequest 
     * @param {module:api/TasksApi~getTasksTasksGetCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link module:model/TasksResponse}
     */
    getTasksTasksGet(tasksRequest, callback) {
      let postBody = tasksRequest;
      // verify the required parameter 'tasksRequest' is set
      if (tasksRequest === undefined || tasksRequest === null) {
        throw new Error("Missing the required parameter 'tasksRequest' when calling getTasksTasksGet");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
      };

      let authNames = ['OAuth2PasswordBearer'];
      let contentTypes = ['application/json'];
      let accepts = ['application/json'];
      let returnType = TasksResponse;
      return this.apiClient.callApi(
        '/tasks/', 'GET',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }

    /**
     * Callback function to receive the result of the uploadTaskTasksUploadPost operation.
     * @callback module:api/TasksApi~uploadTaskTasksUploadPostCallback
     * @param {String} error Error message, if any.
     * @param {Object} data The data returned by the service call.
     * @param {String} response The complete HTTP response.
     */

    /**
     * Upload Task
     * @param {File} inFile 
     * @param {module:api/TasksApi~uploadTaskTasksUploadPostCallback} callback The callback function, accepting three arguments: error, data, response
     * data is of type: {@link Object}
     */
    uploadTaskTasksUploadPost(inFile, callback) {
      let postBody = null;
      // verify the required parameter 'inFile' is set
      if (inFile === undefined || inFile === null) {
        throw new Error("Missing the required parameter 'inFile' when calling uploadTaskTasksUploadPost");
      }

      let pathParams = {
      };
      let queryParams = {
      };
      let headerParams = {
      };
      let formParams = {
        'in_file': inFile
      };

      let authNames = ['OAuth2PasswordBearer'];
      let contentTypes = ['multipart/form-data'];
      let accepts = ['application/json'];
      let returnType = Object;
      return this.apiClient.callApi(
        '/tasks/upload', 'POST',
        pathParams, queryParams, headerParams, formParams, postBody,
        authNames, contentTypes, accepts, returnType, null, callback
      );
    }


}
